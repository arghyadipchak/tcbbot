from fetch_crackwatch import *
from pymongo import MongoClient
from time import sleep

client = MongoClient()
crackwatch = client.crackwatch
cracked = crackwatch.cracked

time_stamp = ""

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