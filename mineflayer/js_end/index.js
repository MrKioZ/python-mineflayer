const yargs = require('yargs');
const mineflayer = require('mineflayer');
const WebSocket = require('ws');

const argv = yargs
    .command('start', 'starts a new bot', {
        username: {
            description: 'the username of the bot',
            alias: 'u',
            type: 'string',
        }
    })
    .option('host', {
        alias: 'h',
        description: 'the minecraft\'s server address',
        type: 'string',
    }).option('port', {
        alias: 'p',
        description: 'the port of the minecraft server',
        type: 'int'
    }).option('whost', {
        alias: 'wh',
        description: 'the port of the websocket',
        type: 'int'
    }).option('wport', {
        alias: 'wp',
        description: 'the port of the websocket',
        type: 'int'
    }).option('securedwebsocket',  {
        alias: 'wss',
        description: 'use the secured websocket protocol',
        type: 'boolean'
    })
    .help()
    .argv;
  
const bot = mineflayer.createBot({
    host: argv.host, // optional
    username: argv.username,
    port: argv.port, // optional
    version: "1.16.4", // version
})

if (argv.wss){
  const ws = new WebSocket(`wss://${argv.whost}:${argv.wport}`);
} else{
  const ws = new WebSocket(`ws://${argv.whost}:${argv.wport}`);
}

ws.on('open', function open() {
  console.log('connected');
  ws.send(Date.now());
});

ws.on('close', function close() {
  console.log('disconnected');
});

ws.on('message', function incoming(data) {
  console.log(`Roundtrip time: ${Date.now() - data} ms`);

  setTimeout(function timeout() {
    ws.send(Date.now());
  }, 500);
});