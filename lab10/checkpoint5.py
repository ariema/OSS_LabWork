#!/usr/bin/env python3
import random
import datetime
from pymongo import MongoClient
client = MongoClient()

db = client.mongo_db_lab

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    all_definitions = db.definitions.find()
    
    ids = []
    for definition in all_definitions:
        ids.append(definition["_id"])
    random_id = random.choice(ids)

    timestamp = datetime.datetime.utcnow()

    db.definitions.update_one(
        { "_id": random_id },
        { "$push": { "dates": timestamp } })

    updated_def = db.definitions.find_one({ "_id": random_id })
    return updated_def


if __name__ == '__main__':
    print(random_word_requester())
