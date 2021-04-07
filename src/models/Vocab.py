import aiohttp
import re
import json

ANKI_CONNECT_URL = "http://192.168.1.251:8765/"
SPANISHDICT_URL = "https://www.spanishdict.com/translate"
INGLES_WORD_FETCH_URL = "https://playground.ingles.com/dictionary/inflections/es?wordId="

class Vocab:
    def __init__(self, spanish):
        self.spanish = spanish
    
    async def lookup(self, session):
        url = f"{SPANISHDICT_URL}/{self.spanish}"
        print(f"url for word is {url}")
        async with session.get(url) as response:
            word_data = re.findall(r"window.SD_COMPONENT_DATA = (.*);", await response.text())[0]
            if word_data is None:
                raise Exception("No matches found")
            
            word_dict = json.loads(word_data)

            props = word_dict["resultCardHeaderProps"]["headwordAndQuickdefsProps"]
            word_type = word_dict["sdDictionaryResultsProps"]["entry"]["neodict"][0]["posGroups"][0]["posDisplay"]["name"]
            examples = word_dict["sdDictionaryResultsProps"]["entry"]["neodict"][0]["posGroups"][0]["senses"][0]["translations"][0]["examples"]
            if props is None or word_type is None or examples is None:
                raise Exception("Word must have props, vocab word type and examples")
            
            self.word_type = word_type
            self.audio = self.upload_audio(props)
            self.english = props["quickdef1"]["textToPronounce"]
            self.examples = examples

    def upload_audio(self, props):
        return props["headword"]["audioUrl"]
