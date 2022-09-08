# Hugin API Twitter Bot
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

HUGIN_API_DOMAIN = 'api.hugin.chat'

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
    # Sets scheduling for when to execute the creation tweets
    schedule.every().monday.at("12:00").do(get_total_board_messages())
    schedule.every().tuesday.at("12:00").do(get_total_hashtags())
    
def get_total_board_messages():
    # API call to Hugin Cache to obtain total amount of board messages
    r = requests.get(f'https://{HUGIN_API_DOMAIN}/api/v1/posts')
    data = r.json()
    total_messages = data['totalItems']
    
    create_tweet(f'Currently rocking {total_messages} messages stored in Official Hugin Cache 🔥')

def get_total_hashtags():
    # API call to Hugin Cache to obtain total amount of hashtags
    r = requests.get(f'https://{HUGIN_API_DOMAIN}/api/v1/hashtags')
    data = r.json()
    total_hashtags = data['totalItems']
    
    create_tweet(f'{total_hashtags} on Official Hugin API! ⚡')

if __name__ == '__main__':
    main()