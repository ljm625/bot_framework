#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 11:43 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : expectParser.py
# @Software: PyCharm

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

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
        if person_email== config.BOT_ACCOUNT:
            spark.send_message("Hi all, this is GimmeBOT :D",room_id)
        else:
            person_name=args['data']['personDisplayName']
            spark.send_message("Hello "+str(person_name)+", Welcome to this cool Spark Room :D",room_id)
        return 204