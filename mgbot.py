import tweepy
from time import sleep
#from credentials import *
#from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

consumer_key = 'gkks6GmyA074vMMWtOmQVVQ7XY'
consumer_secret = 'gkzAhCMmXBFZzX7Qc2WjXz6KdGQ7tOrGkXrtfgJ77IWL9HNCVpd'
access_token = '11596770023-ulleOXmHe0YyzXY0tEn7ZHAxiGs67WlKCYWFYl1'
access_token_secret = 'gdcDdUIb3H4pIo4NRZjbJmtIRr8JXA4SGN1e57Z1do2VqD'

QUERY = 'dobleg5_twitch'


LIKE = True


FOLLOW = False


SLEEP_TIME = 10

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

while 1:
    for tweet in tweepy.Cursor(api.user_timeline, id=QUERY).items(10):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)

            # Favorite the tweet
            if LIKE and str(tweet.created_at) > '2021-03-25 16:17:06':
                tweet.favorite()
                print(str(tweet.created_at))
                print('Favorited the tweet')

            # Follow the user who tweeted
            # check that bot is not already following the user
            # if FOLLOW:
            #   if not tweet.user.following:
            #       tweet.user.follow()
            #      print('Followed the user')



        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    sleep(SLEEP_TIME)
