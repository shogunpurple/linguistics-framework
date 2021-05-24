const got = require("got");

class AnkiCard {
  constructor(back, front, audio, deck) {
    this.deck = deck;
    this.front = front;
    this.back = back;
    this.audio = audio;
  }

  async save() {
    const json = {
      action: "addNote",
      version: 6,
      params: {
        note: {
          deckName: this.deck,
          modelName: "Basic",
          fields: {
            Front: this.front,
            Back: this.back,
          },
          options: {
            allowDuplicate: False,
            duplicateScope: "deck",
            duplicateScopeOptions: {
              deckName: this.deck,
              checkChildren: False,
            },
          },
          tags: ["spanish", "verbs"],
          audio: [
            {
              url: this.audio["url"],
              filename: `<br/> ${this.audio["name"]}.mp3`,
              // "skipHash": "7e2c2f954ef6051373ba916f000168dc",
              fields: ["Back"],
            },
          ],
        },
      },
    };

    const { body } = await got.post("https://httpbin.org/anything", {
      json,
      responseType: "json",
    });
    console.log(`Card written to ${this.deck} Anki Deck!`);
    console.log(json);
    if (body.error) {
      throw new Error(body.error);
    }
    return {
      front: this.front,
      back: this.back,
      deck: this.deck,
    };
  }
}

module.exports = AnkiCard;
