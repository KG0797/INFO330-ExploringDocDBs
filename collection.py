import sqlite3
import pymongo 
import json

mongoClient = pymongo.MongoClient("mongodb://localhost/pokemon")

database_names = mongoClient.list_database_names()
for i in database_names:
    print(i)
    
# set db
pokemonDB = mongoClient['pokemondb']

#set col
pokemonColl = pokemonDB['pokemon_data']

#find all documents 
documents=pokemonColl.find()
for i in documents:
    print(i)
 
conn=sqlite3.connect(r"C:\Users\Katherine Guo\Desktop\info330\INFO330-CreatingRelations2\pokemon.db")
cursor=conn.cursor()

for cnt in range(801):
    cursor.execute('select pokedex_number,name,abilities,type1,type2,hp, attack, defense, speed, sp_attack, sp_defense from imported_pokemon_data where pokedex_number = {}'.format(cnt+1))
    row=list(cursor.fetchone())

    columns=[column[0] for column in cursor.description]

    json_obj={}
    for i in range(len(columns)):
        if columns[i] == 'pokedex_number':
            json_obj[columns[i]]=int(row[i])
        else:
            json_obj[columns[i]]=row[i]
    json_str=json.dumps(json_obj)
    json_data=json.loads(json_str)
    x=pokemonColl.insert_one(json_data)
  
documents=pokemonColl.find()
for i in documents:
    print(i)
