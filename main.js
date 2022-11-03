// The official Hugin API Twitter bot
// Written by TechyGuy17 based on the original python implementation by Mjovanc
// Version 0.0.2
// For license, view the license file

const { TwitterApi } = require('twitter-api-v2');
require('dotenv').config();
const cron = require("node-cron");

const client = new TwitterApi({
    appKey: process.env.APPKEY,
    appSecret: process.env.APPSECRET,
    accessToken: process.env.ACCESSTOKEN,
    accessSecret: process.env.ACCESSSECRET,
})

async function sendToTwitter(message) {
    return await client.v2.tweet(message)
}

async function sendReplytoTwitter(message, id) {
    return await client.v2.reply(message, id)
}

async function getStats() {
    await fetch('https://api.hugin.chat/api/v1/posts')
        .then((response) => {
            return response.json()
        }).then(async (json) => {
            let postAmount = json.total_items
            postMessage = '*TESTING!!* Currently rocking ' + postAmount + ' messages stored in Official Hugin API 🔥 #kryptokrona'
            let response = await sendToTwitter(postMessage)
            let id = response.data.id

            await fetch('https://api.hugin.chat/api/v1/posts-encrypted')
                .then((response) => {
                    return response.json()
                }).then(async (json) => {
                    let encryptedAmount = json.total_items
                    encryptedMessage = 'We also currently have ' + encryptedAmount + ' encrypted messages in the database'
                    let response = await sendReplytoTwitter(encryptedMessage, id)
                })

            await fetch('https://api.hugin.chat/api/v1/statistics/boards/popular')
                .then((response) => { 
                    return response.json()
                }).then(async (json) => {
                    let popularBoard = await json.statistics[0].board
                    let boardPosts = await json.statistics[0].posts
                    boardMessage = 'The most popular board at the moment is "' + popularBoard + '" with a total of ' + boardPosts + ' posts!'
                    sendReplytoTwitter(boardMessage, id)
                })
        })
}

cron.schedule("0 12 * * *", function () {
    console.log("Running todays task")
    getStats()
})