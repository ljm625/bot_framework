#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 3:09 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : main.py
# @Software: PyCharm

# This is the main app for parsing the spark webhook.

import traceback
from pprint import pprint

from flask_cors import CORS, cross_origin
import config
from flask import Flask
from flask_restful import Resource, Api, reqparse

from expectParser import ExpectParser
from keywords import EXPECT_LIST
from mainParser import MainParser
from sentenceGenerator import SentenceGenerator
from sparkAPI import SparkAPI
from syntaxNetParse import SyntaxParser

app = Flask(__name__)
CORS(app)

api = Api(app)

EXPECT_OBJECTS={}

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
        self.reqparse.add_argument('data', type=dict, required=True, help='Data is a required field.',
                                   location='json')
        args = self.reqparse.parse_args()
        msg_id=args['data']['id']
        room_id=args['data']['roomId']
        person_id=args['data']['personId']
        person_email=args['data']['personEmail']
        time=args['data']['created']
        # Now we need to retrieve this message.
        if person_email==config.BOT_ACCOUNT:
            # I don't want to receive infinite messages lol
            return 204
        spark=SparkAPI()
        message=spark.get_message(msg_id)
        synparser = SyntaxParser()
        result = synparser.parse_sentence([message])
        pprint(result)
        pos_tag, dep = synparser.tokenize(result[0])
        print(pos_tag)
        print(dep)
        generator = SentenceGenerator()
        if room_id in EXPECT_OBJECTS:
            expect = EXPECT_OBJECTS[room_id]
            expect.parse(result)
            if not expect.expect_params():
                # All done
                reply=[]
                reply.append(generator.generate_service_review(expect.get_params()))
                global  EXPECT_OBJECTS
                del EXPECT_OBJECTS[room_id]
                reply.append("I will start to execute the service for you. Please wait a few minutes.")
            else:
                reply=[]
                reply.append(generator.generate_service_review(expect.get_params()))
                reply.append(generator.generate_param_request(expect.expect_params()))
        else:
            parser = MainParser(message)
            action = parser.make_category()
            if action in EXPECT_LIST:
                expect = ExpectParser(room_id, 'add_space')
                reply=[]
                reply.append('Sure I can definitely help you on that :D')
                expect.parse(result)
                global EXPECT_OBJECTS
                EXPECT_OBJECTS[room_id]=expect
                reply.append(generator.generate_param_request(expect.expect_params()))
            else:
                reply=generator.generate(action)
        if type(reply)==list:
            for msg in reply:
                spark.send_message(msg,room_id)
        elif type(reply)==str or type(reply)==unicode:
            spark.send_message(reply, room_id)
        return 204


class RoomParser(Resource):

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
        self.reqparse.add_argument('data', type=dict, required=True, help='Data is a required field.',
                                   location='json')
        args = self.reqparse.parse_args()
        msg_id=args['data']['id']
        room_id=args['data']['roomId']
        person_id=args['data']['personId']
        person_email=args['data']['personEmail']
        time=args['data']['created']
        spark=SparkAPI()
        print "New Room Detected"
        # print spark.get_message(msg_id)
        if person_email==config.BOT_ACCOUNT:
            spark.send_message("Hi all, this is GimmeBOT :D",room_id)
        else:
            person_name=args['data']['personDisplayName']
            spark.send_message("Hello "+str(person_name)+", Welcome to this cool Spark Room :D",room_id)
        return 204

api.add_resource(MessageParser, '/api/v1/message')
api.add_resource(RoomParser, '/api/v1/room')


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,debug=True)
