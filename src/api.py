import aiohttp
from models import Verb, AnkiCard, Vocab

async def save_verb(verb, tense):
    async with aiohttp.ClientSession() as session:
        verb_object = Verb.Verb(verb, tense=tense)
        await verb.lookup(session)
        anki_card = AnkiCard.AnkiCard(
            front=f"{verb.spanish} ({verb.tense})",
            back=f"<b>{verb.spanish} - to {verb.english}</b>" + "<br /> <br />" + "<br />".join(verb.conjugation),
            audio={ 'url': verb.audio, 'name': verb.english },
            deck="Spanish Verbs"
        )
        return await anki_card.save(session)

def read_verb_list(tense):
    verb_file = open("words/verbs.txt")
    verbs = [Verb.Verb(verb, tense=tense) for verb in verb_file]
    for verb in verbs:
        pass
        # anki_card = AnkiCard.AnkiCard(
        #     front=f"to {verb.english} ({verb.tense})",
        #     back=f"<b>{verb.spanish}</b>" + "<br /> <br />" + "<br />".join(verb.conjugation),
        #     audio={ 'url': verb.audio, 'name': verb.english },
        #     deck="Spanish Verbs"
        # )
        # anki_card.save()

def read_vocabulary():
    vocab_file = open("words/vocabulary.txt")
    words = [Vocab.Vocab(word) for word in vocab_file]
    for word in words:
        pass
        # anki_card = AnkiCard.AnkiCard(
        #     front=f"{word.spanish}",
        #     back=f"<b>{word.spanish} - {word.english} </b> " + "<br /> <br />" + "<br />".join(word.conjugation),
        #     audio={ 'url': word.audio, 'name': word.english },
        #     deck="Spanish Verbs"
        # )
        # anki_card.save()

# def save_verb(spanish, tense):
#     verb = Verb.Verb(spanish, tense=tense)
#     anki_card = AnkiCard.AnkiCard(
#         front=f"to {verb.english} ({verb.tense})",
#         back=f"<b>{verb.spanish}</b>" + "<br /> <br />" + "<br />".join(verb.conjugation),
#         audio={ 'url': verb.audio, 'name': verb.english },
#         deck="Spanish Verbs"
#     )
#     anki_card.save()
