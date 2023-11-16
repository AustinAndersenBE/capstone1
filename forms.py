from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class SentenceForm(FlaskForm):
    sentence = TextAreaField('Sentence', id='sentence', validators=[DataRequired(), Length(min=1, max=500)])
    vocab_words = StringField('Vocab Words', id='vocab_words', validators=[DataRequired(), Length(min=1, max=200)])