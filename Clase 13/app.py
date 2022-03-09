from flask import Flask, json
from pymongo import MongoClient
import settings
from os import environ

app = Flask(__name__)

USER = environ['USRM']
PASS = environ['PASS']
HOST = environ['HOST']
BASE = environ['BASE']

client = MongoClient("mongodb+srv://"+USER+":"+PASS+"@"+HOST+"/"+BASE+"?retryWrites=true&w=majority")

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
@app.route('/api/tweets')
def getTweets():

    bigdata = client['bigdata']
    tweets = bigdata['tweets']

    los_tweets = tweets.find()

    for tweet in los_tweets:

        print( tweet['id_str'] )

    return '{ "rta" : "ok" }'

if __name__ == '__main__':
    app.run( port = 3030, host = "0.0.0.0" )