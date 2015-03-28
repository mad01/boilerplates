#!/usr/bin/env python
import unittest
import json
import yaml
import os
from pymongo import MongoClient
from requests import put, get
from lib import salt


def checkAccess(oid, password='', host=''):
    data = {"oid": oid, "key": password}
    return get('http://' + host + ':5000/api/protected', data=data)


class TestRestGetCalls(unittest.TestCase):

    @classmethod       
    def setUpClass(self):
        confFile = file('tests/test_salt.yaml', 'r')
        conf = yaml.load(confFile)
        self.mongo = conf.get('mongoDB').get('host')
        self.api = conf.get('api').get('host')
        self.key = "foo"
        self.user = "bar"
        userDoc = salt.addUser(
            self.user,
            password=self.key,
            mongo=self.mongo
        )
        self.oid = userDoc.get("userObjectId")

    @classmethod       
    def tearDownClass(self):
        pass

    def testAccessValidKey(self):
        httpGet = checkAccess(self.oid, password=self.key, host=self.api)
        self.assertEqual(200, httpGet.status_code)

    def testAccessInValidKey(self):
        httpGet = checkAccess(self.oid, password="foobar", host=self.api)
        self.assertEqual(401, httpGet.status_code)


if __name__ == '__main__':
    unittest.main()
