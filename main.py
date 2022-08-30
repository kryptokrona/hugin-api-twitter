# Hugin Cache Twitter Bot
#
# Author: Marcus Cvjeticanin
# Location: Växjö, Sweden
# Website: https://github.com/mjovanc
# Project URL: https://github.com/kryptokrona/hugin-cache-twitter
# Release: 0.0.1

import tweepy

from dotenv import load_dotenv

load_dotenv()

def main():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

    # Create API object
    api = tweepy.API(auth)

def create_tweet(message):
    api.update_status(message)

if __name__ == '__main__':
    main()