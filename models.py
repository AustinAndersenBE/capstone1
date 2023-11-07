from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    sentences = relationship('Sentence', backref='user')

class Vocab(db.Model):
    __tablename__ = 'vocab'
    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    sentences = relationship('Sentence', secondary='sentence_vocab', backref='vocab_words')

class SentenceVocab(db.Model):
    __tablename__ = 'sentence_vocab'
    sentence_id = Column(Integer, ForeignKey('sentences.id'), primary_key=True)
    vocab_id = Column(Integer, ForeignKey('vocab.id'), primary_key=True)

class Sentence(db.Model):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    sentence = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    vocab_words = relationship('Vocab', secondary='sentence_vocab', back_populates='sentences')

class Definition(db.Model):
    __tablename__ = 'definitions'
    id = Column(Integer, primary_key=True)
    definition = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    vocab_id = Column(Integer, ForeignKey('vocab.id'))


