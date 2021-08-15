const Koa = require('koa');
const api = require("./api")
const app = new Koa();

const PORT = process.env.PORT || 3000

app.use(api.routes())

app.listen(3000, () => {
  console.log("Linguistics framework running on " + PORT)
});