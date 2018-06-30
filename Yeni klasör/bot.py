import tweepy
from time import sleep
import random
from secret import *

#Essentials
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Creating API Instance
api = tweepy.API(auth)


quotes = open('text.txt', 'rt')
file_lines = quotes.readlines()
quotes.close()



#Tweet a line every given time.
def randomtweet():
    for line in file_lines:
        try:
            print(line)
            if line != '\n':
                (api.update_status(line))
                sleep(10)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

randomtweet()









