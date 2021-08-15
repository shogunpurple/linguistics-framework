
const SPANISHDICT_URL = "https://www.spanishdict.com/conjugate"

const Tense = {
  PRESENT: "presentIndicative",
  PRETERITE: "preteritIndicative",
  IMPERFECT: "imperfectIndicative",
  SUBJUNCTIVE: "presentSubjunctive",
  IMPERFECT_SUBJUNCTIVE: "imperfectSubjunctive"
}

class Verb {
  constructor(spanish, tense=Tense.PRESENT) {
    this.spanish = spanish
    this.tense = tense
  }

  async lookup() {
    const url = `${SPANISHDICT_URL}/${this.spanish}`
    console.log(`URL for verb is ${url}`)

    const { body } = await got(url);
    const wordDataRgx = /window.SD_COMPONENT_DATA = (.*);/
    const verbData = body.match(wordDataRgx)
    if (!verbData) {
      throw new Error("No matches found")
    }

    // TODO: test if this works
  }
}

