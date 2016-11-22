#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 3:17 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : sparkAPI.py
# @Software: PyCharm


# This file is used to do the spark requests. For example post a message or query a message
import requests

import config


class SparkAPI(object):
    def __init__(self,spark_url=config.SPARK_URL,spark_token=config.SPARK_TOKEN):
        self.url=spark_url
        self.token=spark_token
        self.headers={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+self.token}

    def get_message(self,msg_id):
        def buildUrl():
            return self.url+'messages/'+str(msg_id)
        resp=requests.get(buildUrl(),headers=self.headers)
        if resp.status_code >= 300:
            print "Error in the api"
            print resp.status_code
            resp.raise_for_status()
        else:
            if resp.json() is not None:
                return resp.json()['text']

