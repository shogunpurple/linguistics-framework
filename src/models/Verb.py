import re
import json
import asyncio
import enum
import requests
import aiohttp

ANKI_CONNECT_URL = "http://192.168.1.251:8765/"
SPANISHDICT_URL = "https://www.spanishdict.com/conjugate"

class Tense(enum.Enum):
    PRESENT = "presentIndicative"
    PRETERITE = "preteritIndicative"
    IMPERFECT = "imperfectIndicative"
    SUBJUNCTIVE = "presentSubjunctive"

class Verb:
    def __init__(self, spanish, tense="presentIndicative"):
        print("Word is " + spanish)
        self.spanish = spanish
        self.tense = tense
    
    async def lookup(self, session):
        url = f"{SPANISHDICT_URL}/{self.spanish}"
        print(f"url for verb is {url}")
        async with session.get(url) as response:
            verb_data = re.findall(r"window.SD_COMPONENT_DATA = (.*);", await response.text())[0]
            if verb_data is None:
                raise Exception("No matches found")
            
            verb_dict = json.loads(verb_data)

            props = verb_dict["resultCardHeaderProps"]["headwordAndQuickdefsProps"]
            if props is None:
                raise Exception("Verb does not contain relevant lookup metadata.")
            
            self.audio = self.upload_audio(props)
            self.english = props["quickdef1"]["textToPronounce"]
            self.conjugation = [f"{form['pronoun']} {form['word']}" for form in verb_dict["verb"]["paradigms"][self.tense]] 
            self.gerund = verb_dict["verb"]["gerund"]["word"]

    def upload_audio(self, props):
        # TODO: fetch the audio pronounciation using polly
        return props["headword"]["audioUrl"]