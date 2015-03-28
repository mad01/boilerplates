#!/usr/bin/env python
import yaml
from flask import Flask, abort
from flask.ext.restful import Api, Resource, reqparse
from lib import mongo
from lib import salt

app = Flask(__name__)
api = Api(app)
confFile = file('restApi.yaml', 'r')
conf = yaml.load(confFile)


class protected(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('oid')
        self.reqparse.add_argument('key')
        self.mongo = conf.get('mongoDB').get('host')
        super(protected, self).__init__()

    def get(self):
        args = self.reqparse.parse_args(strict=True)
        validateCheck = salt.validateUserKey(
            userObjectId=args.oid,
            password=args.key,
            mongo=self.mongo
        )
        if validateCheck:
            return {"key": "valid"}
        else:
            abort(401)


api.add_resource(protected, '/api/protected')

if __name__ == '__main__':
    app.run(debug=True)
