const { Probot } = require("probot");

const probot = new Probot({
  privateKey: process.env.GITHUB_PRIVATE_KEY
})
