exports.saveVerb = async (ctx, next) => {
  try {
    const body = ctx.request.body
    const tense = body.tense

    for (let tense in Object.keys(Tense)) {
      // throw
    }

    const verb = new Verb()
      // verb_object = Verb.Verb(verb, tense=tense)
      // try:
      //     await verb_object.lookup(session)
      // except Exception:
      //     err = f"Error looking up verb: {verb}"
      //     raise Exception(err) 

      // anki_card = AnkiCard.AnkiCard(
      //     front=f"{verb_object.spanish} ({verb_object.tense})",
      //     back=f"<b>{verb_object.spanish} - to {verb_object.english}</b>" + "<br /> <br />" + "<br />".join(verb_object.conjugation),
      //     audio={ 'url': verb_object.audio, 'name': verb_object.english },
      //     deck="Spanish Verbs"
      // )
      // return await anki_card.save(session)
  } catch (err) {
    console.error(err)
    ctx.throw(500, err)
  }
    // try:
    //     body = request.get_json()
    //     tense = body["tense"]

    //     # Check that the tense in the request is valid
    //     allowed_tenses = [tense.value for tense in list(Verb.Tense)]
    //     if tense not in allowed_tenses:
    //         return jsonify({ "error": f"Tense not valid. Must be one of {', '.join(allowed_tenses)}"}), 400

    //     asyncio.set_event_loop(asyncio.new_event_loop())
    //     loop = asyncio.get_event_loop()
    //     result = loop.run_until_complete(api.save_verb(body["word"], body["tense"]))
    //     loop.close()
    //     return jsonify(result)
    // except Exception as e:
    //     app.logger.error(e)
    //     return jsonify({ "error": str(e) }), 500
}

exports.saveVocab = async (ctx, next) => {
  // stuff
}