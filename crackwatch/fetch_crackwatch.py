def fetch(*args, **kwargs):
    import requests
    return requests.get('https://api.crackwatch.com/api/games', kwargs).json()    

def fetch_gen(*args, **kwargs):
    if 'page' not in kwargs: kwargs['page'] = 0
    while True:
        request_json = fetch(*args, **kwargs)
        if not request_json: break
        yield request_json
        kwargs['page']+= 1


fetch_cracked = lambda *args,**kwargs: fetch(*args, **kwargs, is_released = True)
fetch_uncracked = lambda *args,**kwargs: fetch(*args, **kwargs, is_released = False)

def fetch_cracked_gen(*args, **kwargs):
    if 'page' not in kwargs: kwargs['page'] = 0
    while True:
        request_json = fetch_cracked(**kwargs)
        if not request_json: break
        yield request_json
        kwargs['page']+= 1

def fetch_uncracked_gen(*args, **kwargs):
    if 'page' not in kwargs: kwargs['page'] = 0
    while True:
        request_json = fetch_uncracked(**kwargs)
        if not request_json: break
        yield request_json
        kwargs['page']+= 1