const {TwitterApi} = require('twitter-api-v2');
require('dotenv').config();
const cron = require("node-cron");

const client = new TwitterApi({
    appKey: process.env.APPKEY,
    appSecret: process.env.APPSECRET,
    accessToken: process.env.ACCESSTOKEN,
    accessSecret: process.env.ACCESSSECRET,
});

async function sendPostAmountToTwitter(postAmount) {
    client.v2.tweet('Currently rocking ' + postAmount + ' messages stored in Official Hugin API 🔥' ).then((val) => {
        console.log(val)
        console.log("success")
    }).catch((err) => {
        console.log(err)
    })
}
async function getPostStats() {
    
    await fetch('https://api.hugin.chat/api/v1/posts')
    .then((response) => {
        return response.json()
    }).then((json) => {
        let postAmount = json.total_items
        console.log(postAmount)
        sendPostAmountToTwitter(postAmount)
    })
}

cron.schedule("0 12 * * *", function () {
    console.log("Running todays task")
    getPostStats()
});