const mineflayer = require('mineflayer');

// ipc.js <host> <port> <username> <version>
const data = JSON.parse(process.argv[2])
const host = data['host']
const port = data['port']
const username = data['username']
// const version = data['version']

const bot = mineflayer.createBot({
    host: host, // optional
    username: username,
    port: port,       // optional
    version: "1.16.4", // version
})

