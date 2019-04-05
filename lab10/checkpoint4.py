#!/usr/bin/env python3
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()

if __name__ == '__main__':
    db = client.mongo_db_lab
    definitions = db.definitions

    #find all
    print("fetch all")
    for d in definitions.find():
        print(d)
    print()
    #find one word
    print("fetch one")
    print(definitions.find_one())
    print()

    #find one specific record
    print("fetch one specific record")
    print(definitions.find_one({"word": "Blow Away"}))
    print()

    #find by object id
    print("fetch one by id")
    id = ObjectId("56fe9e22bad6b23cde07b8b9")
    print(db.definitions.find_one({ "_id": id}))
    print()
    #insert record
    print("insert liger")
    result = definitions.insert_one({"word": "Liger", "definition": "Half lion and half tiger"})
    print("Insert id {}".format(result.inserted_id))
