from fetch_crackwatch import *
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from time import sleep
from datetime import datetime

load_dotenv()
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DB = os.getenv('DB_NAME')
db_client = MongoClient(username = USER, password = PASSWORD, authSource = DB)

time_stamp = str(datetime.now())
print("TimeStamp:", time_stamp)

collection = db_client[DB].allgames
for k in [0, 1]:
    fetcher = (fetch_cracked_gen, fetch_uncracked_gen)[k]()
    count = 0
    while True:
        games = next(fetcher)
        if not games: break
        count+= len(games)
        print(("Cracked:", "Uncracked:")[k], count)
        for game in games:
            game.update({'lastUpdated': time_stamp, "crackStatus": ("Cracked", "Uncracked")[k]})
            if not collection.update_one({'_id': game['_id']}, {'$set': game}).modified_count:
                collection.insert_one(game)
        sleep(1)
collection.delete_many({'lastUpdated': {'$ne': time_stamp}})