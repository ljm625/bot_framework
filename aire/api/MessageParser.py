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

import aire.config as config
from aire.orch import Orch


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
        Orch().message_parse(args)
        return 204
