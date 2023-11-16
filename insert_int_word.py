from app import app
from models import db, Vocab

app.app_context().push()  # push an application context

def insert_vocab_words():
    intermediate_words = [
    'ameliorate', 'circumvent', 'cogent', 'conundrum', 'dichotomy',
    'disparate', 'efficacy', 'enigmatic', 'epitome', 'equivocal',
    'exacerbate', 'fortitude', 'idiosyncratic', 'impetus', 'incongruous',
    'indelible', 'insidious', 'juxtapose', 'mitigate', 'pedagogical',
    'precipitate', 'quintessential', 'repertoire', 'ubiquitous', 'venerable'
]

    for word in intermediate_words:
        existing_word = Vocab.query.filter_by(word=word).first()
        if existing_word is None:
            new_word = Vocab(word=word, level='intermediate')
            db.session.add(new_word)

    db.session.commit()

if __name__ == "__main__":
    insert_vocab_words()