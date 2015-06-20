#!/usr/bin/env python

import json
import hashlib
import pymongo

try:
    conn = pymongo.MongoClient()
    print('Connected Successfully')
except:
    print 'Error'

db = conn['test']
collection = db['users']

def signup(data):
    uhash = hashlib.sha1(data['pass']).hexdigest()
                            #    {_id:'a@gmail.com', pass:'123'}
    data.pop('pass',None)
    data['token'] = uhash
    data['items'] = {'food':[], 'clothes': [], 'money': [], 'books': []}
    try:
        collection.insert(data)
    except pymongo.errors.DuplicateKeyError as d:
        return None
    return uhash


def login(data):
    email = data['_id']
    token = data.get('token')
    resp =  list(collection.find({'_id': email,'token':token}))
    if data.get('pass'):
        token = hashlib.sha1(data['pass']).hexdigest()
        # check hash
        resp =  list(collection.find({'_id': email,'token':token}))
    if resp:
        return token
    else:
        return 0

def insert_items(data):
    #item_type = data["item_type"]
    #if item_type == "food":
    if 'food' in data.keys():
        collection.update({'_id': data['_id']}, {'$push':{'items.food': data['food']}})
        # insert food
        
    elif 'clothes' in data.keys():
        collection.update({'_id': data['_id']}, {'$push':{'items.clothes': data['clothes']}})
    
    elif 'money' in data.keys():
        collection.update({'_id': data['_id']}, {'$push':{'items.money': data['money']}})
        
    
    elif 'books' in data.keys():
        collection.update({'_id': data['_id']}, {'$push':{'items.books': data['books']}})
    
    else:
        pass


        


