import aiohttp
from models import Verb, AnkiCard, Vocab

async def save_verb(verb, tense):
    async with aiohttp.ClientSession() as session:
        verb_object = Verb.Verb(verb, tense=tense)
        try:
            await verb_object.lookup(session)
        except Exception:
            err = f"Error looking up verb: {verb}"
            raise Exception(err) 

        anki_card = AnkiCard.AnkiCard(
            front=f"{verb_object.spanish} ({verb_object.tense})",
            back=f"<b>{verb_object.spanish} - to {verb_object.english}</b>" + "<br /> <br />" + "<br />".join(verb_object.conjugation),
            audio={ 'url': verb_object.audio, 'name': verb_object.english },
            deck="Spanish Verbs"
        )
        return await anki_card.save(session)

async def save_vocabulary(word):
    async with aiohttp.ClientSession() as session:
        word_object = Vocab.Vocab(word)
        try:
            await word_object.lookup(session)
        except Exception as e:
            err = f"Error looking up word: {word}. {str(e)}"
            raise Exception(err) 
        
        back = f"""
            <b>{word_object.spanish} ({word_object.word_type}) - </b> {word_object.english} <br /> <br />
            
            {'<br />'.join([f"{example['textEn']} <br /> <b>{example['textEs']}</b>" for example in word_object.examples])}
        """

        anki_card = AnkiCard.AnkiCard(
            front=word_object.spanish,
            back=back,
            audio={ 'url': word_object.audio, 'name': word_object.english },
            deck="Spanish Vocabulary"
        )
        return await anki_card.save(session)

def read_verb_list(tense):
    verb_file = open("words/verbs.txt")
    verbs = [Verb.Verb(verb, tense=tense) for verb in verb_file]
    for verb in verbs:
        save_verb(verb, tense)

def read_vocabulary_list():
    vocab_file = open("words/vocabulary.txt")
    words = [Vocab.Vocab(word) for word in vocab_file]
    for word in words:
        save_vocabulary(word)