from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    sentences = relationship('Sentence', back_populates='user', cascade="all, delete-orphan")
    upvoted_sentences = relationship('Sentence', secondary='sentence_upvotes', backref='upvoted_by')


class Vocab(db.Model):
    __tablename__ = 'vocab'
    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    level = Column(String, nullable=False)  # 'beginner', 'intermediate', 'advanced'
    sentences = relationship('Sentence', secondary='sentence_vocab', back_populates='vocab_words')

class SentenceVocab(db.Model):
    __tablename__ = 'sentence_vocab'
    sentence_id = Column(Integer, ForeignKey('sentences.id', ondelete='CASCADE'), primary_key=True)
    vocab_id = Column(Integer, ForeignKey('vocab.id'), primary_key=True)

class Sentence(db.Model):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    sentence = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    upvotes = Column(Integer, default=0)
    user = relationship('User', back_populates='sentences')
    vocab_words = relationship(
        'Vocab',
        secondary='sentence_vocab',
        back_populates='sentences',  
        primaryjoin="Sentence.id==SentenceVocab.sentence_id",  
        secondaryjoin="Vocab.id==SentenceVocab.vocab_id",
    )

class SentenceUpvotes(db.Model):
    __tablename__ = 'sentence_upvotes'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    sentence_id = Column(Integer, ForeignKey('sentences.id', ondelete='CASCADE'), primary_key=True)


class Definition(db.Model):
    __tablename__ = 'definitions'
    id = Column(Integer, primary_key=True)
    definition = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    vocab_id = Column(Integer, ForeignKey('vocab.id'))
    
def connect_db(app):
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


