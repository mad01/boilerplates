#!/usr/bin/env python
from passlib import apps
from mongo import createOrUpdateUser
from mongo import getUser


def addUser(username, password='', mongo=''):
    """add user and a salted password to mongoDB"""
    passwordSalted = apps.custom_app_context.encrypt(password)
    userObjectId = createOrUpdateUser(
        username,
        saltedKey=passwordSalted,
        host=mongo,
        database='endpoints'
    )
    return {"userObjectId": userObjectId}


def validateUserKey(userObjectId, password='', mongo=''):
    """validate user password returns boolean"""
    salt = getUser(
        userObjectId,
        host=mongo,
        database="endpoints"
    )
    return apps.custom_app_context.verify(password, salt.get('saltedKey'))


