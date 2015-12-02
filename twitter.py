# This program is designed by Richard Limo to display Twitter items as an assignment in AI programming.

import sys # For file manipulations 
import tweepy # To get twitter authentication and realtime items
from tweepy import OAuthHandler
import json # creation and manipulation of json files

#introducing authentication Keys for connection to twitter account.
#Each twitter account has unique Keys
#The files will be saved as json files i.e. Home timeline, Twitter Frieends and user Timeline
#The same files will be displayed.

consumer_key = "ADD CUSTOMER KEY CODE"
consumer_secret = "ADD CUSTOMER SECRET CODE"
access_token = "ADD ACCESS TOKEN CODE"
access_token_secret = "ADD ACCESS TOKEN SECRET"

#Replace the above Customer key, Customer Secret, Access Token and Access Token Secrets with your own.

set_key = tweepy.OAuthHandler(consumer_key, consumer_secret)
set_key.set_access_token(access_token, access_token_secret)
app = tweepy.API(set_key)

# This function displays and saves the Twitter items
def display_and_save(tweet_item,file_name):
    print(json.dumps(tweet_item)+'\n')
    with open(file_name, 'w') as outfile:
     json.dump(tweet_item, outfile)

#This section saves and displays twitter Home Timeline
print '+----------------------------------------------------+'
print '|                                                    |'
print '|              Twitter Home Timeline                 |'
print '|                                                    |'
print '+----------------------------------------------------+'

for Home in tweepy.Cursor(app.home_timeline).items():
  try:
    display_and_save(Home._json,'Home.txt') 
    break
  except ValueError:
    print "Error"

#This section saves and displays Twitter friends
print '+----------------------------------------------------+'
print '|                                                    |'
print '|              Twitter Friends                       |'
print '|                                                    |'
print '+----------------------------------------------------+'

for Friends in tweepy.Cursor(app.friends).items():
  try:
    display_and_save(Friends._json,'Friend.txt')
    break
  except ValueError:
    print "Error"

#this section will save and display user Timeline items
print '+----------------------------------------------------+'
print '|                                                    |'
print '|              Twitter User Timeline                 |'
print '|                                                    |'
print '+----------------------------------------------------+'

for Timeline in tweepy.Cursor(app.user_timeline).items():
  try:
    display_and_save(Timeline._json,'Timeline.txt')
    break
  except ValueError:
    print "Error"
# end of Program
