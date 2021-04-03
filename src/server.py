from flask import Flask, request
from api import *
app = Flask(__name__)

@app.route('/phrase')
def save_phrase():
    return 'Hello World!'

@app.route('/word')
def save_word():
    return 'Hello World!'

@app.route('/verb', methods=["POST"])
async def save_verb():
    body = request.get_json()
    return await api.save_verb(body["verb"], body["tense"])

if __name__ == '__main__':
    app.run()