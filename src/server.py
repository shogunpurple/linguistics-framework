from flask import Flask, request, jsonify
from models import Verb
import asyncio
import api

app = Flask(__name__)

@app.route('/api/phrase', methods=["POST"])
def save_phrase():
    return 'Hello World!'

@app.route('/api/vocab', methods=["POST"])
def save_vocab():
    try:
        body = request.get_json()
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(api.save_vocab(body["word"]))
        loop.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({ "error": e })

@app.route('/api/verb', methods=["POST"])
def save_verb():
    try:
        body = request.get_json()
        tense = body["tense"]
        allowed_tenses = [tense.value for tense in list(Verb.Tense)]
        if tense not in allowed_tenses:
            return jsonify({ "error": f"Tense not valid. Must be one of {', '.join(allowed_tenses)}"})

        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(api.save_verb(body["verb"], body["tense"]))
        loop.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({ "error": e })

if __name__ == '__main__':
    app.run(host="0.0.0.0")