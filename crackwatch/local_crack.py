from fetch_crackwatch import *
from pymongo import MongoClient
from time import sleep
from datetime import datetime

time_stamp = str(datetime.now())

client = MongoClient()
crackwatch = client.crackwatch
cracked = crackwatch.cracked

fetcher = fetch_cracked_gen()
while True:
    games = next(fetcher)
    if not games: break
    for game in games:
        game['lastUpdated'] = time_stamp
        if not cracked.update_one({'_id': game['_id']}, {'$set': game}):
            cracked.insert_one(game)
    sleep(1)
cracked.delete_many({'lastUpdated': {'$ne': time_stamp}})

uncracked = crackwatch.cracked

fetcher = fetch_uncracked_gen()
while True:
    games = next(fetcher)
    if not games: break
    for game in games:
        game['lastUpdated'] = time_stamp
        if not uncracked.update_one({'_id': game['_id']}, {'$set': game}):
            uncracked.insert_one(game)
    sleep(1)
uncracked.delete_many({'lastUpdated': {'$ne': time_stamp}})