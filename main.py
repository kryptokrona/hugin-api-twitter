# Hugin Cache Twitter Bot
#
# Author: Marcus Cvjeticanin
# Location: Växjö, Sweden
# Website: https://github.com/mjovanc
# Project URL: https://github.com/kryptokrona/hugin-cache-twitter
# Release: 0.0.1

import tweepy
import os
import schedule
import requests
import json

from dotenv import load_dotenv

load_dotenv()

HUGIN_CACHE_DOMAIN = 'cache.hugin.chat'

def main():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        daemon()
    except Exception as e:
        print("Error during authentication", str(e))

def create_tweet(message):
    api.update_status(message)

def daemon():
    schedule.every().monday.at("12:00").do(total_posts())
    schedule.every().tuesday.at("12:00").do(get_top_hashtag())
    
def get_total_board_messages():
    r = requests.get(f'https://{HUGIN_CACHE_DOMAIN}/api/v1/posts')
    data = r.json()
    total_messages = data['totalItems']
    
    create_tweet(f'Currently rocking {total_messages} messages stored in Official Hugin Cache 🔥')

def get_total_hashtags():
    r = requests.get(f'https://{HUGIN_CACHE_DOMAIN}/api/v1/hashtags')
    data = r.json()
    total_hashtags = data['totalItems']
    
    create_tweet(f'{total_hashtags} on Hugin Cache! ⚡')

if __name__ == '__main__':
    main()