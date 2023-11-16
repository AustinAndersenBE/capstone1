from app import app
from models import db, Vocab

app.app_context().push()  # push an application context

def insert_vocab_words():
    advanced_words = [
    'adumbrate', 'anathema', 'calumny', 'capricious', 'enervate',
    'evince', 'excoriate', 'expurgate', 'extirpate', 'fecund',
    'insouciant', 'liminal', 'mendacious', 'obdurate', 'pellucid',
    'penurious', 'peremptory', 'juxtapose', 'prognosticate', 'puerile',
    'recondite', 'sanguine', 'salient', 'scurrilous', 'voluble', 'untenable'
    ]

    for word in advanced_words:
        existing_word = Vocab.query.filter_by(word=word).first()
        if existing_word is None:
            new_word = Vocab(word=word, level='advanced')
            db.session.add(new_word)

    db.session.commit()

if __name__ == "__main__":
    insert_vocab_words()