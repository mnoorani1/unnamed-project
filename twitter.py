import tweepy
from tweepy import OAuthHandler
from datetime import datetime, date

api_key = "4Af1ppNg7fioJScSUgpny309r"
api_secret_key = "NXW5MsIFWq6zEBxvOprmimjxJ3BGeE7sJfG6X1L2mO4Uk3L5xh"
access_token = "461295220-XYVMGoOHQQOz86rtiaqI88XgTlDVvlMwraVg0VQz"
access_token_secret = "Zb1BT2BOXRAMYXZxfnB87YfuDj7QAUqovxzWAmuxj6NQj"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

recent_tweet = api.user_timeline(screen_name = "junaidakram83", count=2, exclude_replies = True, include_rts = False, tweet_mode="extended")
print(recent_tweet[0].full_text)
print(recent_tweet[0].entities)