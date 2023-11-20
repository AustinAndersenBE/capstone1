import os
from flask import Flask, render_template, request, flash, redirect, session, g, url_for, jsonify
from flask_limiter import Limiter
from flask_bcrypt import Bcrypt
from functools import wraps
from forms import RegistrationForm, LoginForm, SentenceForm
from models import User, connect_db, db, Vocab, Definition, Sentence, SentenceVocab, SentenceUpvotes
from helpers import authenticate_user, create_user
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import joinedload
from string import punctuation
from flask_migrate import Migrate

app = Flask(__name__)

migrate = Migrate(app, db)

def get_remote_address():
    return request.remote_addr

# not using a limiter for now
# limiter = Limiter(app)
# limiter.key_func = get_remote_address
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///vocab_project')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
app.config['TESTING'] = False

connect_db(app)


def get_current_user_key():
    return "curr_user"

@app.context_processor
def make_utility_functions_available():
    return dict(get_current_user_key=get_current_user_key)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash("Access unauthorized.", "danger")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.before_request
def add_user_to_g():
    curr_user_key = get_current_user_key()
    if curr_user_key in session:
        g.user = User.query.get(session[curr_user_key])
    else:
        g.user = None


##### My APIs ######

#API endpoint to generate 7 random words from our database
@app.route('/api/vocab/<level>', methods=['GET'])
#@limiter.limit("10/minute")
def get_vocab(level):
    words = Vocab.query.filter_by(level=level).order_by(func.random()).limit(7).all()
    return jsonify([{'id': word.id, 'word': word.word} for word in words])


#API endpoint to get the definitions of a word
@app.route('/api/definitions/<word_id>', methods=['GET'])
def get_definitions(word_id):
    definitions = Definition.query.filter_by(vocab_id=word_id).all()
    return jsonify([{
        'definition': definition.definition,
        'is_correct': definition.is_correct
    } for definition in definitions])

@app.route('/api/vocab_words', methods=['GET'])
def get_vocab_all():
    vocab_words = Vocab.query.all()
    return jsonify([vocab.word for vocab in vocab_words])


# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = authenticate_user(email, password)  
        if user:
            session[get_current_user_key()] = user.id
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('home'))


#User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_with_same_username = User.query.filter_by(username=form.username.data).first()
        user_with_same_email = User.query.filter_by(email=form.email.data).first()
        if user_with_same_username:
            flash('Username already taken. Please choose a different one.', 'danger')
            return render_template('register.html', form=form)
        if user_with_same_email:
            flash('Email already in use. Please use a different one.', 'danger')
            return render_template('register.html', form=form)
        user = create_user(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        session[get_current_user_key()] = user.id
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/')
def home():
    return render_template('home.html')


##Core of the site

#Learn page
@app.route('/learn')
def learn():
    return render_template('learn.html')

#Sentence page
@app.route('/sentences')
@login_required
def sentences():
    sentences = Sentence.query.options(joinedload(Sentence.vocab_words), joinedload(Sentence.user)).all()
    return render_template('sentences.html', sentences=sentences)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

#Sentence form page
#server side processing of submitting a new sentence
@app.route('/sentences/new', methods=['GET', 'POST'])
@login_required
def create_sentence():
    form = SentenceForm()
    if form.validate_on_submit():
        sentence_text = form.sentence.data 
        sentence = Sentence(sentence=sentence_text, user_id=g.user.id) #add sentence to DB first
        db.session.add(sentence)
        db.session.commit()
        
        # to check for vocab words in the sentence, we make sentence lowercase and remove punctuation
        processed_sentence = sentence_text.lower()
        processed_sentence = processed_sentence.translate(str.maketrans('', '', punctuation))
        
        vocab_words = set(word.strip() for word in form.vocab_words.data.lower().split(',')) # from user input, create a set of vocab. (delineate based on comma)
        vocab_objects = Vocab.query.filter(Vocab.word.in_(vocab_words)).all() #filters Vocab table to retrieve entries where word matches the vocab_words
        vocab_dict = {vocab.word: vocab for vocab in vocab_objects} #create a dictionary, key is the word and value is the vocab object
        
        for word in vocab_words:
            if word in processed_sentence:  # check if vocab word is in the sentence
                vocab = vocab_dict.get(word)
                if vocab: #if there is a vocab object
                    sentence_vocab = SentenceVocab(sentence_id=sentence.id, vocab_id=vocab.id)  #if we confirm that the vocab exists in the db, we then add the association entry
                    db.session.add(sentence_vocab)
                
        db.session.commit()        
        return redirect(url_for('sentences'))
    
    return render_template('new_sentence_form.html', form=form)

#Upvotes
@app.route('/upvote/<int:sentence_id>', methods=['POST'])
@login_required
def upvote(sentence_id):
    sentence = Sentence.query.get(sentence_id)
    if sentence:
        # Check if the current user has already upvoted the sentence
        existing_upvote = SentenceUpvotes.query.filter_by(
            user_id=g.user.id, 
            sentence_id=sentence_id
        ).first()

        if not existing_upvote:
            new_upvote = SentenceUpvotes(user_id=g.user.id, sentence_id=sentence_id)
            db.session.add(new_upvote)

            sentence.upvotes = (sentence.upvotes or 0) + 1

            db.session.commit()
    return redirect(url_for('sentences'))


#Deleting sentences
@app.route('/delete_sentence/<int:sentence_id>', methods=['POST'])
@login_required
def delete_sentence(sentence_id):
    sentence = Sentence.query.get(sentence_id)
    if sentence and sentence.user_id == g.user.id:
        db.session.delete(sentence)
        db.session.commit()
    return redirect(url_for('sentences'))