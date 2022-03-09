from flask import Flask, json
from pymongo import MongoClient
from os import environ
from urllib.parse import urlencode
import settings

app = Flask(__name__)

USER = environ['USRM']
PASS = environ['PASS']
HOST = environ['HOST']
BASE = environ['BASE']

params = {
 'retryWrites':'true',
 'w':'majority',
 'ssl':'true',
 'ssl_cert_reqs':'CERT_NONE'   
}

client = MongoClient("mongodb+srv://"+USER+":"+PASS+"@"+HOST+"/"+BASE+"?"+urlencode(params))

@app.route('/')
def hello_flask():
    return 'Hola desde Flask :D'
###################
@app.route('/users')
def usersTwitter():
    users = [
        { 'name' : 'smessina_' },
        { 'name' : 'eanttech' },
        { 'name' : 'TinchoLutter' },
        { 'name' : 'bitcoinArg' }
    ]

    response = app.response_class( response = json.dumps(users), status = 200, mimetype = 'application/json' )

    return response

###################
@app.route('/users/<path>')
def searchTwitter(path):
    if path == 'personas':
        response = "Aca deberia mostrar un JSON de personas"
    elif path == 'empresas':
        response = "Aca deberia mostrar un JSON de empresas"
    else:
        response = "No puedo mostrar lo que estás pidiendo :P"
    
    return response

###################
@app.route('/api/tweets/<user>/<limit>')
def getTweets(user, limit):

    bigdata = client['bigdata']
    tweets = bigdata['tweets']

    # Sin ternario
    '''
    if limit != None and limit.isnumeric():
        limit = int(limit)
    else:
        limit = 0
    '''
    # Con ternario
    limit = int(limit) if limit != None and limit.isnumeric() else 0

    los_tweets = tweets.find({ 'in_reply_to_screen_name' : user }).limit( limit )

    response = [] if los_tweets.count() > 0 else [{ 'ok' : False, 'mgs' : 'User not found' }]
 
    for tweet in los_tweets:

        el_tweet = {
            'id' : tweet['id_str'],
            'user' : tweet['in_reply_to_screen_name'],
            'message' : tweet['full_text']
        }

        response.append( el_tweet )

    return app.response_class( response = json.dumps(response), status = 200, mimetype = 'application/json' )

if __name__ == '__main__':
    app.run( port = 3030, host = "0.0.0.0" )