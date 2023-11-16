from app import app
from models import db, Vocab, Definition

app.app_context().push()  # push an application context

# Define the words and their definitions

words_definitions = {
    'adumbrate': [
        ('To give a sketchy outline or reveal partially', True),
        ('To enlighten with knowledge', False),
        ('To enhance or make more attractive', False),
        ('To repair or restore to good condition', False),
    ],
    'anathema': [
        ('Something or someone that one vehemently dislikes', True),
        ('A traditional or commonly accepted belief', False),
        ('An element that causes relaxation', False),
        ('A method of organizing books in a library', False),
    ],
    'calumny': [
        ('A false and malicious statement designed to injure the reputation of someone or something', True),
        ('A type of ancient sculpture', False),
        ('A ceremony involving the lighting of candles', False),
        ('A mathematical term used to describe a set of numbers', False),
    ],
    'capricious': [
        ('Given to sudden and unaccountable changes of mood or behavior', True),
        ('Relating to financial matters', False),
        ('A term used to describe a dense forest', False),
        ('A characteristic of being consistent and unchanging', False),
    ],
    'enervate': [
        ('To cause someone to feel drained of energy or vitality; weaken', True),
        ('To decorate with bright colors', False),
        ('To invest with legal rights', False),
        ('To preserve food by removing moisture', False),
    ],
    'evince': [
        ('To show or express clearly; to make evident', True),
        ('To approve or sanction', False),
        ('To estimate the value of something', False),
        ('To engage in a lengthy discussion', False),
    ],
    'excoriate': [
        ('To criticize severely', True),
        ('To excavate or dig up', False),
        ('To heal or remedy a disease', False),
        ('To coat with a protective layer', False),
    ],
    'expurgate': [
        ('To remove matter thought to be objectionable or unsuitable', True),
        ('To expand or open up', False),
        ('To purge air from a system', False),
        ('To explain or clarify a statement', False),
    ],
    'extirpate': [
        ('To destroy or remove completely', True),
        ('To integrate or combine', False),
        ('To instigate or start an action', False),
        ('To tie up or secure firmly', False),
    ],
    'fecund': [
        ('Fruitful in offspring or vegetation; fertile', True),
        ('Showing a lack of judgment or experience', False),
        ('Capable of producing a great deal of heat', False),
        ('Pertaining to a league or alliance', False),
    ],
    'insouciant': [
        ('Showing a casual lack of concern; indifferent', True),
        ('Unable to sleep or rest', False),
        ('Being in a state of agitation', False),
        ('Susceptible to stains', False),
    ],
    'liminal': [
        ('Of or relating to a transitional or initial stage of a process', True),
        ('Limiting or controlling access or passage', False),
        ('Relating to the sea or tides', False),
        ('Describing an object with a smooth, shiny surface', False),
    ],
    'mendacious': [
        ('Not telling the truth; lying', True),
        ('Relating to the process of healing', False),
        ('Having a pleasant and distinctive smell', False),
        ('Relating to the science of measurement', False),
    ],
    'obdurate': [
        ('Stubbornly refusing to change one\'s opinion or course of action', True),
        ('Relating to the study of birds', False),
        ('Acting in a confused or disoriented manner', False),
        ('Engaging in or reflecting deep thought', False),
    ],
    'pellucid': [
        ('Translucently clear', True),
        ('Capable of being shaped or molded', False),
        ('Having a sharp, strong quality especially related to smell', False),
        ('Relating to the countryside; rural', False),
    ],
    'penurious': [
        ('Extremely poor; poverty-stricken', True),
        ('Given to spending money freely and foolishly', False),
        ('Characterized by a great deal of wind', False),
        ('Having a high position or level of authority', False),
    ],
    'peremptory': [
        ('Insisting on immediate attention or obedience, especially in a brusquely imperious way', True),
        ('Related to or characteristic of an emperor or empire', False),
        ('Being undecided or hesitant', False),
        ('Acting in a lazy or indifferent manner', False),
    ],
    'juxtapose': [
        ('To place or deal with close together for contrasting effect', True),
        ('To confuse or perplex', False),
        ('To postpone or delay', False),
        ('To replicate or duplicate an action', False),
    ],
    'prognosticate': [
        ('To forecast or predict (something future) from present indications or signs; prophesy', True),
        ('To celebrate with lively and noisy festivities', False),
        ('To engage in a detailed and complex discussion', False),
        ('To mediate between opposing parties', False),
    ],
    'puerile': [
        ('Childishly silly and trivial', True),
        ('Relating to or denoting a period of work', False),
        ('Capable of enduring difficult conditions; hardy', False),
        ('Able to move quickly and easily', False),
    ],
    'recondite': [
        ('(Of a subject or knowledge) little known; abstruse', True),
        ('Requiring a lot of care, attention, and effort', False),
        ('Related to the art of public speaking', False),
        ('Covered with or resembling small bubbles as from boiling', False),
    ],
    'sanguine': [
        ('Optimistic or positive, especially in an apparently bad or difficult situation', True),
        ('Relating to or involving bloodshed', False),
        ('Sour or astringent in taste', False),
        ('Describing a style of art that uses exaggerated motion', False),
    ],
    'salient': [
        ('Most noticeable or important', True),
        ('Pertaining to the production of salt', False),
        ('Capable of leaping or jumping', False),
        ('Showing a tendency to repeat something previously said', False),
    ],
    'scurrilous': [
        ('Making or spreading scandalous claims about someone with the intention of damaging their reputation', True),
        ('Moving in a twisting or snake-like or worm-like fashion', False),
        ('Relating to the sky or the heavens', False),
        ('Marked by precise accordance with details', False),
    ],
    'voluble': [
        ('Speaking or spoken incessantly and fluently', True),
        ('Capable of being easily poured or spread', False),
        ('Having a bulky or heavy appearance', False),
        ('Relating to volcanic activity', False),
    ],
    'untenable': [
        ('(Especially of a position or view) not able to be maintained or defended against attack or objection', True),
        ('Incapable of being passed through or penetrated', False),
        ('Not capable of being mixed or combined', False),
        ('Lacking the necessary skills or abilities for a particular task or job', False),
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

