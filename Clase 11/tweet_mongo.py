from pymongo import MongoClient
import tweepy
import json
import pprint
from urllib.parse import urlencode

consumer_key='Dlx6x09dcDBfCxQJQkqdiPpkX'
consumer_secret='6pICWUhmQTycUWTGxvdGWNmjkNgsD9yhND7XPygIF5XxUBDgb6'
access_token='740566466139918336-fEfTAmiEXuytp2IYmumPNyhyONkcUUb'
access_token_secret='DNB5yE49GQfVvMKpLzu1HfVYNcPkSRhhhcjJtpFuf3sqQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = []

USER="federico"
PASS="36716172"
HOST="mordor.9k0e0.mongodb.net"
BASE="bigdata"

params = {
'retryWrites':'true',
'w':'majority',
'ssl':'true',
'ssl_cert_reqs':'CERT_NONE'

}

cliente = MongoClient("mongodb+srv://"+USER+":"+PASS+"@"+HOST+"/"+BASE+"?"+urlencode(params))

bd = cliente['bigdata']
coleccion = bd['tweets']
try:
    ultimo_tweet = coleccion.find_one(sort=[("id", -1)])['id']
except:
    ultimo_tweet = None

for tweet in tweepy.Cursor(api.user_timeline, since_id=ultimo_tweet, screen_name = 'alferdez', tweet_mode = 'extended').items(2000):
    #pprint.pprint(tweet._json)#Para ver toda la info de los tutis
    tweet_dic = tweet._json
    tweets.append(tweet_dic)
    print("tweet capturado")

coleccion.insert_many(tweets)

