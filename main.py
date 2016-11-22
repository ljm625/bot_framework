#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 3:09 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : main.py
# @Software: PyCharm

# This is the main app for parsing the spark webhook.

import traceback
from flask_cors import CORS, cross_origin

from flask import Flask
from flask_restful import Resource, Api, reqparse

from sparkAPI import SparkAPI

app = Flask(__name__)
CORS(app)

api = Api(app)

class MessageParser(Resource):

    def post(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=str, required=True, help='id is a required field.',
                                   location='json')
        self.reqparse.add_argument('name', type=str, required=True, help='Description is a required field.',
                                   location='json')
        self.reqparse.add_argument('resource', type=str, required=True, help='Description is a required field.',
                                   location='json')
        self.reqparse.add_argument('event', type=str, required=True, help='Description is a required field.',
                                   location='json')
        self.reqparse.add_argument('filter', type=str, required=True, help='Description is a required field.',
                                   location='json')
        self.reqparse.add_argument('data', type=dict, required=True, help='Description is a required field.',
                                   location='json')
        args = self.reqparse.parse_args()
        msg_id=args['data']['id']
        room_id=args['data']['roomId']
        person_id=args['data']['personId']
        person_email=args['data']['personEmail']
        time=args['data']['created']
        # Now we need to retrieve this message.
        spark=SparkAPI()
        print spark.get_message(msg_id)
        return 204

api.add_resource(MessageParser, '/api/v1/message')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,debug=True)
