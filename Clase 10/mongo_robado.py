from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={
    'precio': {
        '$lt': 800
    }
}
sort=list({
    'precio': -1
}.items())
limit=10

result = client['universidad']['libros'].find(
  filter=filter,
  sort=sort,
  limit=limit
)

for libro in result:
    print(libro)