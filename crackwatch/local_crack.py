from fetch_crackwatch import *
from pymongo import MongoClient
from time import sleep
from datetime import datetime

time_stamp = str(datetime.now())
print("TimeStamp:", time_stamp)

client = MongoClient()

# cracked = client.crackwatch.cracked
# fetcher = fetch_cracked_gen()
# cracked_count = 0
# while True:
#     games = next(fetcher)
#     if not games: break
#     cracked_count+= len(games)
#     print("Cracked:", cracked_count)
#     for game in games:
#         game['lastUpdated'] = time_stamp
#         if not cracked.update_one({'_id': game['_id']}, {'$set': game}).modified_count:
#             cracked.insert_one(game)
#     sleep(1)
# cracked.delete_many({'lastUpdated': {'$ne': time_stamp}})

# uncracked = client.crackwatch.uncracked
# fetcher = fetch_uncracked_gen()
# uncracked_count = 0
# while True:
#     games = next(fetcher)
#     if not games: break
#     uncracked_count+= len(games)
#     print("Uncracked:", uncracked_count)
#     for game in games:
#         game['lastUpdated'] = time_stamp
#         if not uncracked.update_one({'_id': game['_id']}, {'$set': game}).modified_count:
#             uncracked.insert_one(game)
#     sleep(1)
# uncracked.delete_many({'lastUpdated': {'$ne': time_stamp}})

collection = client.crackwatch.allgames
for k in [0, 1]:
    fetcher = (fetch_cracked_gen, fetch_uncracked_gen)[k]()
    count = 0
    while True:
        games = next(fetcher)
        if not games: break
        count+= len(games)
        print(("Cracked", "Uncracked")[k], count)
        for game in games:
            game.update({'lastUpdated': time_stamp, "crackStatus": ("Cracked", "Uncracked")[k]})
            if not collection.update_one({'_id': game['_id']}, {'$set': game}).modified_count:
                collection.insert_one(game)
        sleep(1)
collection.delete_many({'lastUpdated': {'$ne': time_stamp}})