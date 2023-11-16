from app import app
from models import db, Vocab

app.app_context().push()  # push an application context

def insert_vocab_words():
    beginner_words = [
    'breeze', 'steep', 'vivid', 'harvest', 'thread', 
    'bargain', 'dusk', 'gleam', 'mild', 'sturdy', 
    'thrifty', 'vast', 'weary', 'pledge', 'glee', 
    'loom', 'migrate', 'nurture', 'quest', 'ripe', 
    'savor', 'tread', 'utmost', 'venture', 'wharf'
]

    for word in beginner_words:
        existing_word = Vocab.query.filter_by(word=word).first()
        if existing_word is None:
            new_word = Vocab(word=word, level='beginner')
            db.session.add(new_word)

    db.session.commit()

if __name__ == "__main__":
    insert_vocab_words()