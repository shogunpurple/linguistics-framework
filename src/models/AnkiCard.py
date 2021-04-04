import requests
import aiohttp
import enum

ANKI_CONNECT_URL = "http://192.168.1.251:8765/"

class Decks(enum.Enum):
    VERBS = "Spanish Verbs"
    VOCAB = "Spanish Vocabulary"
    PHRASES = "Spanish Phrases"

class AnkiCard():
    def __init__(self, back, front, audio, deck):
        self.deck = deck
        self.front = front
        self.back = back
        self.audio = audio
    
    async def save(self, session):
        body = {
                "action": "addNote",
                "version": 6,
                "params": {
                    "note": {
                        "deckName": self.deck,
                        "modelName": "Basic",
                        "fields": {
                            "Front": self.front,
                            "Back":  self.back 
                        },
                        "options": {
                            "allowDuplicate": False,
                            "duplicateScope": "deck",
                            "duplicateScopeOptions": {
                                "deckName": self.deck,
                                "checkChildren": False
                            }
                        },
                        "tags": [
                            "spanish",
                            "verbs"
                        ],
                        "audio": [{
                            "url": self.audio["url"],
                            "filename": f"<br/> {self.audio['name']}.mp3",
                            # "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                            "fields": [
                                "Back"
                            ]
                        }],
                        # "video": [{
                        #     "url": "https://cdn.videvo.net/videvo_files/video/free/2015-06/small_watermarked/Contador_Glam_preview.mp4",
                        #     "filename": "countdown.mp4",
                        #     "skipHash": "4117e8aab0d37534d9c8eac362388bbe",
                        #     "fields": [
                        #         "Back"
                        #     ]
                        # }],
                    #     "picture": [{
                    #         "url": self.image,
                    #         "filename": f"{self.spanish}_conjugation.jpg",
                    #         "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                    #         "fields": [
                    #             "Back"
                    #         ]
                        # }]
                }
            }
        }
        # save the card
        async with session.post(ANKI_CONNECT_URL, json=body) as response:
            json = await response.json(content_type='text/json')
            print(f"Card written to {self.deck} Anki Deck!")
            print(json)
            if json["error"] is not None:
                raise Exception(json["error"])
            return {
                "front": self.front,
                "back": self.back,
                "deck": self.deck
            }