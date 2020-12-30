from datetime import datetime
from os import getenv
from pymongo import MongoClient
from time import sleep

def fetch(*args, **kwargs):
    import requests
    return requests.get('https://api.crackwatch.com/api/games', kwargs).json()    

def fetch_gen(*args, **kwargs):
    if 'page' not in kwargs: kwargs['page'] = 0
    while True:
        request_json = fetch(*args, **kwargs)
        #if not request_json: break
        yield request_json
        kwargs['page']+= 1

fetch_cracked = lambda *args,**kwargs: fetch(*args, **kwargs, is_cracked = 'true')
fetch_uncracked = lambda *args,**kwargs: fetch(*args, **kwargs, is_cracked = 'false')

def fetch_cracked_gen(*args, **kwargs):
    if 'page' not in kwargs: kwargs['page'] = 0
    while True:
        request_json = fetch_cracked(**kwargs)
        #if not request_json: break
        yield request_json
        kwargs['page']+= 1

def fetch_uncracked_gen(*args, **kwargs):
    if 'page' not in kwargs: kwargs['page'] = 0
    while True:
        request_json = fetch_uncracked(**kwargs)
        #if not request_json: break
        yield request_json
        kwargs['page']+= 1

def run_bot(HOST, USER, PSWD, AUTH, DB):
    db_client = MongoClient(host = [HOST], username = USER, password = PSWD, authSource = AUTH)

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

if __name__ == '__main__':
    from os import getenv
    HOST = getenv('DB_HOST')
    USER = getenv('DB_USER')
    PSWD = getenv('DB_PASSWORD')
    AUTH = getenv('DB_AUTH')
    DB = getenv('DB_WORK')
    run_bot(HOST, USER, PSWD, AUTH, DB)

    STIME = getenv('SLEEP_TIME')
    sleep(STIME)