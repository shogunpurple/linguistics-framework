import requests
import re
import json

ANKI_CONNECT_URL = "http://192.168.1.251:8765/"
SPANISHDICT_URL = "https://www.spanishdict.com/conjugate"
INGLES_WORD_FETCH_URL = "https://playground.ingles.com/dictionary/inflections/es?wordId="

class Vocab:
    def __init__(self, spanish):
        self.spanish = spanish
        self.lookup()
    
    def lookup(self):
        url = f"{SPANISHDICT_URL}/{self.spanish}"
        print(f"url for word is {url}")
        response = requests.get(url)
        word_data = re.findall(r"window.SD_COMPONENT_DATA = (.*);", response.text)[0]
        if word_data is None:
            raise Exception("No matches found")
        
        word_dict = json.loads(word_data)

        print(word_dict)

        props = word_dict["resultCardHeaderProps"]["headwordAndQuickdefsProps"]
        if props is None:
            raise Exception
        
        # # get word info
        word_id = props["sdWordRootProps"]["wordId"]
        # word_info = requests.get(f"{INGLES_WORD_FETCH_URL}{word_id}")
        # word_json = word_info.json()

        self.audio = self.upload_audio(props)
        # self.english = props["quickdef1"]["textToPronounce"]
        # self.gender = word_json["data"]["inflectionTypes"][0]["gender"]

    def upload_audio(self, props):
        # TODO: fetch the audio pronounciation using polly
        return props["headword"]["audioUrl"]