const WebSocket = require('ws');

const { NearGoal } = require('mineflayer-pathfinder').goals;
const { Movements } = require('mineflayer-pathfinder');

function IPC(endpoint, bot) {
    
    this.endpoint = endpoint
    this.ws = new WebSocket('ws://' + this.endpoint);
    this.bot = bot
    this.username = bot.username

    this.following = null;

    this.ping = async function() {
        this.ws.send(JSON.stringify({ "username": this.username }))
    }

    this.bot.on('entityMoved', (entity) => {
        if (entity === this.following) {
            const mcData = require('minecraft-data')(this.bot.version);
            this.bot.pathfinder.setMovements(new Movements(this.bot, mcData));
            this.bot.pathfinder.setGoal(new GoalNear(entity.x, entity.y, entity.z, 1));
        }
    });

    this.followEntity = function(entity) {
        this.following = entity
    };

    this.unfollowEntity= function() {
        this.following = null
    };
    
    this.handleResponse = function(response) {
        if (response.action === 'attack') {

            const entity = this.bot.entities[response.extra_data.entity];

            if (entity){
                if (entity === this.bot.entity) return;
                this.bot.pvp.attack(entity);
            }

        } else if (response.action === 'stopattack') {
            this.bot.pvp.stop();
        } else if (response.action === 'chat') {
            this.bot.chat(response.extra_data.content);
        } else if (response.action === 'follow') {
            if (response.extra_data.entity.type === 'player') {
                this.followingEntity(this.bot.players[username].entity)
            }
        } else if (response.action === 'unfollow') {
            thius.unfollowEntity()
        }

        console.log(response)
    }

    this.communicate = async function(payload){
        const response = await axios ({
            url: this.endpoint,
            headers: { "username": this.username },
            data: payload,
            method: "POST"
        })
        return this.handleResponse(response.data)
    }
}

module.exports = IPC;