import tweepy
import json
import pprint
#Link para registrarse en Twitter
#https://developer.twitter.com/en/docs/basics/getting-started
#Tutorial para obtener los tokens
#https://www.ingresosviaweb.com/api-y-token-de-twitter/
# Twitter App Tokens
claves = open('claves.txt')
keys = []
for clave in claves:
    
    clave = clave.strip('\n').split("'")[1::2]

    keys.append(clave[0])

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#%%
# Mi perfil
usuario = api.me()
pprint.pprint(usuario._json)
#%%
# #Otro usuario
otro_usuario = api.get_user("alferdez")
pprint.pprint(otro_usuario._json)
#%%
#Seguidores de un usuario

#Entrega un objeto limitada a 20 elementos (resultados paginados)
seguidores = api.followers(screen_name = 'smessina_')
for seguidor in seguidores:
    print(seguidor._json['screen_name'])

#%%
#Lo utilizo para sobrepasar el límite de 20 en lo que quiera
#api.friends (los que el usuario sigue)
for seguidor in tweepy.Cursor(api.friends, screen_name = 'smessina_').items(100):
       #print(json.dumps(seguidor._json, indent=2))
       nombre = seguidor._json['name']
       print(nombre)

#%%
##timeline todos los twits que posteó el usuario (truncado y sin truncar)
contador = 1
for tweet in tweepy.Cursor(api.user_timeline, screen_name = 'alferdez', tweet_mode = 'extended').items(10):
    print(contador)
    pprint.pprint(tweet._json['id'])#Para ver toda la info de los tutis
    contador += 1
#%%
#Cómo mostrar el texto extendido de los retuits
iden = tweet.id
status = api.get_status(iden, tweet_mode="extended")
try:
    print("Texto completo del retweet:", status.retweeted_status.full_text)
    final =  status.full_text.find(':')
    print("Retweeteado de:", status.full_text[2:final], '\n')
except AttributeError:  # Not a Retweet
    print(status.full_text, '\n')

#%%
#Búsqueda de Twits
for tweet in tweepy.Cursor(api.search, q = 'music', tweet_mode = 'extended').items(20):
      #Sacar lo que quiera del tweet
      print(tweet._json['full_text'])
