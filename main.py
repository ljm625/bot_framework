#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 3:09 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : main.py
# @Software: PyCharm

# This is the main app for parsing the spark webhook.

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from aire.api.MessageParser import MessageParser
# from aire.api.RoomParser import RoomParser

app = Flask(__name__)
CORS(app)

api = Api(app)

EXPECT_OBJECTS={}

api.add_resource(MessageParser, '/api/v1/message')
#api.add_resource(RoomParser, '/api/v1/room')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5050,debug=True)
