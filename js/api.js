const Router = require("koa-router")
const controller = require("./controller")

const router = new Router()

router
  .get("/")
  .post("/api/verb", controller.saveVerb)
  .post("/api/vocabulary", controller.saveVocab)

module.exports = router;