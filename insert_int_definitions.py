from app import app
from models import db, Vocab, Definition

app.app_context().push()  # push an application context

# Define the words and their definitions
words_definitions = {
    'ameliorate': [
        ('To make something better or more bearable', True),
        ('To weaken or reduce in force', False),
        ('A method of preserving food', False),
        ('To disassemble something into smaller parts', False),
    ],
    'circumvent': [
        ('To find a way around an obstacle or rule, usually cleverly or illegally', True),
        ('To apply a protective coating', False),
        ('To invent or bring about something new', False),
        ('To fortify or strengthen against attack', False),
    ],
    'cogent': [
        ('Intellectually convincing or compelling', True),
        ('A gradual decrease in thickness or width of an elongated object', False),
        ('A circular or spiral motion or form', False),
        ('A ceremony of formal investiture whereby an individual assumes an office or position of authority', False),
    ],
    'conundrum': [
        ('A difficult question or riddle, especially one using a play on words in the answer', True),
        ('A state of being pleasantly lost in one\'s thoughts', False),
        ('A traditional story sometimes popularly regarded as historical but not authenticated', False),
        ('A specialist in the study of plant life', False),
    ],
    'dichotomy': [
        ('A division or contrast between two things that are represented as being opposed or entirely different', True),
        ('A chemical substance that changes color in the presence of an acid or a base', False),
        ('The highest point of a mountain', False),
        ('A piece of music written for two performers', False),
    ],
    'disparate': [
        ('Fundamentally distinct or different in kind; entirely dissimilar', True),
        ('Having a smooth, glowing surface', False),
        ('A part of a river where the current is very fast', False),
        ('A moment of sudden and great revelation or realization', False),
    ],
    'efficacy': [
        ('The ability to produce a desired or intended result', True),
        ('An official order or commission to do something', False),
        ('The quality of being loyal or having a strong allegiance to something', False),
        ('A humorous or malicious deception', False),
    ],
    'enigmatic': [
        ('Difficult to interpret or understand; mysterious', True),
        ('Very attentive to and concerned about accuracy and detail', False),
        ('Inclined to lay down principles as undeniably true', False),
        ('A person who is new to a subject, skill, or belief', False),
    ],
    'epitome': [
        ('A person or thing that is a perfect example of a particular quality or type', True),
        ('A machine for shaping wood, metal, or other material', False),
        ('A deep or seemingly bottomless chasm', False),
        ('The action of expelling someone from a property', False),
    ],
    'equivocal': [
        ('Open to more than one interpretation; ambiguous', True),
        ('Moving or capable of moving at high speed', False),
        ('A thing that is helpful or beneficial', False),
        ('A person who publicly supports or recommends a particular cause or policy', False),
    ],
    'exacerbate': [
        ('To make a problem, bad situation, or negative feeling worse', True),
        ('To make a precise replica or model of something', False),
        ('To separate or release from something that is attached or connected', False),
        ('To take part in a contest or competition', False),
    ],
    'fortitude': [
        ('Courage in pain or adversity', True),
        ('An emotional state or reaction', False),
        ('A law regarded as deriving from natural rights that are inherent in human nature', False),
        ('An area of muddy or boggy ground', False),
    ],
    'idiosyncratic': [
        ('Peculiar or individual', True),
        ('A gathering of people for a religious service', False),
        ('A piece of cloth put under a saddle', False),
        ('The state of being unaware or unconscious of what is happening', False),
    ],
    'impetus': [
        ('The force or energy with which a body moves', True),
        ('A sudden loud noise', False),
        ('A vehicle or means of transport', False),
        ('The action of making amends for a wrong or injury', False),
    ],
    'incongruous': [
        ('Not in harmony or keeping with the surroundings or other aspects of something', True),
        ('The occurrence of the same letter or sound at the beginning of adjacent or closely connected words', False),
        ('A method of broadcasting or sending messages', False),
        ('A structure with a roof and walls', False),
    ],
    'indelible': [
        ('Making marks that cannot be removed', True),
        ('Able to be understood from something unsaid or implied', False),
        ('Capable of bending easily without breaking', False),
        ('A person who refrains from indulging in something', False),
    ],
    'insidious': [
        ('Proceeding in a gradual, subtle way, but with harmful effects', True),
        ('To proclaim or declare something officially or formally', False),
        ('To make an agreement legally valid by signing', False),
        ('An increase in the rate or speed of something', False),
    ],
    'juxtapose': [
        ('To place or deal with close together for contrasting effect', True),
        ('To make something seem smaller or less important', False),
        ('To join or combine to form a single entity', False),
        ('To keep something harmful at bay or from happening', False),
    ],
    'mitigate': [
        ('To make less severe, serious, or painful', True),
        ('To prepare and use land for crops or gardening', False),
        ('To confirm or give support to a statement, theory, or finding', False),
        ('To predict something or cause something to happen in advance', False),
    ],
    'pedagogical': [
        ('Relating to teaching or education', True),
        ('A method of preserving food by removing moisture', False),
        ('Characterized by or suggesting the practice of severe self-discipline', False),
        ('Pertaining to the measurement of time', False),
    ],
    'precipitate': [
        ('To cause an event or situation, typically one that is bad or undesirable, to happen suddenly, unexpectedly, or prematurely', True),
        ('To stall or delay proceedings', False),
        ('To extract or obtain something with effort', False),
        ('To give an authority or right to', False),
    ],
    'quintessential': [
        ('Representing the most perfect or typical example of a quality or class', True),
        ('Having five parts of equal importance', False),
        ('Characterized by five repeating events', False),
        ('A collection of five literary or artistic works', False),
    ],
    'repertoire': [
        ('A stock of plays, dances, or pieces that a company or a performer knows or is prepared to perform', True),
        ('A portable shelter', False),
        ('The act of controlling or governing something', False),
        ('An essential or characteristic part of something', False),
    ],
    'ubiquitous': [
        ('Present, appearing, or found everywhere', True),
        ('A small piece or amount of something', False),
        ('Having a strong, distinctive flavor or smell', False),
        ('A person who lives somewhere permanently or on a long-term basis', False),
    ],
    'venerable': [
        ('Accorded a great deal of respect, especially because of age, wisdom, or character', True),
        ('Capable of being changed or formed into something different', False),
        ('Able to be touched or felt', False),
        ('Occurring at irregular intervals or only in a few places', False),
    ],
}


for word, definitions in words_definitions.items():
    vocab = Vocab.query.filter_by(word=word).first()
    if vocab is None:
        print(f"Word {word} not found in database.")
        continue

    for definition, is_correct in definitions:
        defn = Definition(definition=definition, is_correct=is_correct, vocab_id=vocab.id)
        db.session.add(defn)

    db.session.commit()

