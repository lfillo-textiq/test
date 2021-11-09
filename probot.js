const { Probot } = require("probot");

const probot = new Probot({
  privateKey: process.env.GITHUB_PRIVATE_KEY,
  appId: process.env.APP_ID,
  secret: process.env.WEBHOOK_SECRET,
})
