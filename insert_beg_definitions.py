from app import app
from models import db, Vocab, Definition

app.app_context().push()  # push an application context

# Define the words and their definitions
words_definitions = {
    'breeze': [
        ('A gentle and light wind.', True),
        ('A sharp incline of a hill or mountain.', False),
        ('The act of preserving fruit through drying.', False),
        ('A traditional dance originating from Europe.', False),
    ],
    'steep': [
        ('Having a sharp inclination; precipitous.', True),
        ('A type of seasoning used in cooking.', False),
        ('The act of engaging in trade negotiations.', False),
        ('A description for an extremely cold climate.', False),
    ],
    'vivid': [
        ('Producing powerful feelings or strong, clear images in the mind.', True),
        ('A structure used for storage in maritime contexts.', False),
        ('A feeling of extreme tiredness.', False),
        ('A type of bird known for its migratory behavior.', False),
    ],
    'harvest': [
        ('The process of gathering mature crops from the fields.', True),
        ('A type of bird known for its migratory behavior.', False),
        ('A sharp incline of a hill or mountain.', False),
        ('A traditional dance originating from Europe.', False),
    ],
    'thread': [
        ('A long, thin strand of cotton, nylon, or other fibers used in sewing.', True),
        ('A type of seasoning used in cooking.', False),
        ('The act of preserving fruit through drying.', False),
        ('A method of fortifying doors', False),
    ],
    'bargain': [
        ('An agreement between two parties for the purchase or sale of something at a price advantageous to both.', True),
        ('A light mist that appears at dawn.', False),
        ('A small, rounded stone used in landscaping.', False),
        ('The name for a group of stars in the night sky.', False),
    ],
    'dusk': [
        ('The darker stage of twilight, especially in the evening.', True),
        ('A period of time set aside for eating lunch.', False),
        ('The sound made by a large bell.', False),
        ('A tool used for cutting wood.', False),
    ],
    'gleam': [
        ('A flash or beam of light.', True),
        ('A shallow part of a body of water.', False),
        ('The process of fermenting grapes into wine.', False),
        ('An ancient type of currency.', False),
    ],
    'mild': [
        ('Not severe, serious, or harsh.', True),
        ('The outer covering of a ship.', False),
        ('A measurement of distance in the countryside.', False),
        ('A type of heavy machinery used in construction.', False),
    ],
    'sturdy': [
        ('Strongly and solidly built.', True),
        ('A light, powdery substance used in cooking.', False),
        ('A form of ceremonial dance.', False),
        ('A narrow path through the forest.', False),
    ],
    'thrifty': [
        ('Using money and other resources carefully and not wastefully.', True),
        ('A type of spice used in baking.', False),
        ('A term describing a wide open space.', False),
        ('A unit of measurement for liquids.', False),
    ],
    'vast': [
        ('Of very great extent or size; enormous.', True),
        ('A period of time when business activity is very slow.', False),
        ('A type of dessert made with fruit and cream.', False),
        ('A tool used for gripping or bending materials.', False),
    ],
    'weary': [
        ('Feeling or showing tiredness, especially as a result of excessive exertion or lack of sleep.', True),
        ('A ceremony or service held shortly after a person\'s death.', False),
        ('The process by which plants turn sunlight into energy.', False),
        ('A wild, typically small, carnivorous animal.', False),
    ],
    'pledge': [
        ('A solemn promise or undertaking.', True),
        ('A type of fisherman\'s knot.', False),
        ('A period of artistic or literary activity.', False),
        ('A method of arranging flowers artistically.', False),
    ],
    'glee': [
        ('Great delight, especially from one\'s own good fortune or another\'s misfortune.', True),
        ('A method of soil cultivation.', False),
        ('A type of tree that produces acorns.', False),
        ('A form of address for a woman, usually in a foreign language.', False),
    ],
    'loom': [
        ('An apparatus for making fabric by weaving yarn or thread.', True),
        ('A period of time in the afternoon designated for tea and light snacks.', False),
        ('A type of musical instrument.', False),
        ('A method of writing or engraving on a hard surface.', False),
    ],
    'migrate': [
        ('To move from one region or habitat to another, especially regularly according to the seasons.', True),
        ('A kind of thick, heavy fabric used for clothing.', False),
        ('To engage in deep thought or contemplation.', False),
        ('The act of trading goods or services without the exchange of money.', False),
    ],
    'nurture': [
        ('To care for and encourage the growth or development of.', True),
        ('A sturdy, flat-bottomed boat used in shallow waters.', False),
        ('A tall pillar or structure, typically part of a building.', False),
        ('A type of ceremonial procession.', False),
    ],
    'quest': [
        ('A long or arduous search for something.', True),
        ('A shallow container used for cooking food.', False),
        ('A form of quilted garment.', False),
        ('The highest point of a hill or mountain.', False),
    ],
    'ripe': [
        ('(Of fruit or grain) developed to the point of readiness for harvesting and eating.', True),
        ('A term used to describe a well-cooked piece of meat.', False),
        ('A feeling of coldness in the atmosphere.', False),
        ('A device used to capture or kill animals.', False),
    ],
    'savor': [
        ('To taste (good food or drink) and enjoy it completely.', True),
        ('A type of small, fast ship.', False),
        ('A heavy wooden beam used in construction.', False),
        ('A group of actors performing a play.', False),
    ],
    'tread': [
        ('To walk in a specified way.', True),
        ('The sound produced by a clock or watch.', False),
        ('A type of grass that grows in wet places.', False),
        ('A measure of land area, especially in agriculture.', False),
    ],
    'utmost': [
        ('Most extreme; greatest.', True),
        ('A small building, often used as a storehouse.', False),
        ('A detailed map of a small area of land.', False),
        ('A room or building for scientific experiments.', False),
    ],
    'venture': [
        ('A risky or daring journey or undertaking.', True),
        ('A type of bird known for its melodious singing.', False),
        ('A formal agreement between two parties.', False),
        ('A method of fortifying a position or place.', False),
    ],
    'wharf': [
        ('A level quayside area to which a ship may be moored to load and unload.', True),
        ('A feeling of warm, personal attachment or deep affection.', False),
        ('A type of lightweight hat with a brim.', False),
        ('An opening in the wall of a building, typically to let in light and air.', False),
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

