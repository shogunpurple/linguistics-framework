# import sys 
# from models import Verb, AnkiCard, Vocab
# import asyncio
# import aiohttp

# async def read_verb_list(tense):
#     verb_file = open("words/verbs.txt")
#     async with aiohttp.ClientSession() as session:
#         verbs = [Verb.Verb(verb, tense=tense) for verb in verb_file]
#         await asyncio.wait([verb.lookup(session) for verb in verbs])

#         cards = []
#         for verb in verbs:
#             anki_card = AnkiCard.AnkiCard(
#                 front=f"{verb.spanish} ({verb.tense})",
#                 back=f"<b>{verb.spanish} - to {verb.english}</b>" + "<br /> <br />" + "<br />".join(verb.conjugation),
#                 audio={ 'url': verb.audio, 'name': verb.english },
#                 deck="Spanish Verbs"
#             )
#             cards.append(anki_card)
#             await asyncio.wait([card.save(session) for card in cards])

# def read_vocabulary():
#     vocab_file = open("words/vocabulary.txt")
#     words = [Vocab.Vocab(word) for word in vocab_file]
#     for word in words:
#         anki_card = AnkiCard.AnkiCard(
#             front=f"{word.spanish}",
#             back=f"<b>{word.english} </b> " + "<br /> <br />" + "<br />".join(word.examples),
#             audio={ 'url': word.audio, 'name': word.english },
#             deck="Spanish Vocabulary"
#         )
#         print(anki_card)
#         anki_card.save()


# if __name__ == "__main__":
#     # args = sys.argv[1:]
#     # if len(args) == 0:
#     #     raise Exception("No Args Passed")

#     read_vocabulary()
#     # loop = asyncio.get_event_loop()
#     # result = loop.run_until_complete(read_verb_list(Verb.Tense.PRESENT.value))
#     # loop.close()
    
#     # read_verb_list(Verb.Tense.PRETERITE.value)
