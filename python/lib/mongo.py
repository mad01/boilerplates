#!/usr/bin/env python
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId


def createOrUpdateUser(username, saltedKey='', host='', database=''):
    """create or update user"""
    client = MongoClient(host)
    db = client[database]
    checkUser = [doc for doc in db.user.find({"username": username})]
    if checkUser:
        userData = checkUser[0]
        db.user.replace_one(
            {
                "username": username,
                "saltedKey": userData.get('saltedKey'),
            }, {
                "username": username,
                "saltedKey": saltedKey,
                "created": userData.get('created'),
                "updated": datetime.datetime.utcnow()
            }
        )
        userObjectId = [doc for doc in db.user.find({"username": username})][0].get('_id')
        return str(userObjectId)

    else:
        data = {
            "saltedKey": saltedKey,
            "created": datetime.datetime.utcnow(),
            "updated": datetime.datetime.utcnow(),
            "username": username,
        }
        userObjectId = db.user.insert_one(data).inserted_id
        return str(userObjectId)


def getUser(userObjectId, host='', database=''):
    """get user json ducument from mongo"""
    client = MongoClient(host)
    db = client[database]
    return [doc for doc in db.user.find({"_id": ObjectId(userObjectId)})][0]
