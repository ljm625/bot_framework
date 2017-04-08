#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 3:17 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : sparkAPI.py
# @Software: PyCharm


# This file is used to do the spark requests. For example post a message or query a message
import requests

from aire import config
from aire.messenger.MessengerAbstract import MessengerAbstract


class Spark(MessengerAbstract):
    def __init__(self, spark_url=config.SPARK_URL, spark_token=config.SPARK_TOKEN):
        self.url=spark_url
        self.token=spark_token
        self.headers={'Content-type':'application/json; charset=utf-8','Authorization':'Bearer '+self.token}

    @classmethod
    def get_instance(cls, input=None):
        try:
            if(config.SPARK_URL and config.SPARK_TOKEN):
                return cls()
            elif(input.get("SPARK_URL") and input.get("SPARK_TOKEN")):
                return cls(spark_url=input.get("SPARK_URL"),spark_token=input.get("SPARK_TOKEN"))
            else:
                raise Exception("The required settings for Spark Plugin is not fullfilled!")
        except Exception as e:
            print("ERROR : The config is not fullfilled for the plugin. {}".format(e))
            return None

    def get_message(self,input):
        msg_id=input['msg_id']
        def buildUrl():
            return self.url+'messages/'+str(msg_id)
        resp=requests.get(buildUrl(),headers=self.headers)
        if resp.status_code >= 300:
            print("Error in the api")
            print(resp.status_code)
            resp.raise_for_status()
        else:
            if resp.json() is not None:
                return resp.json()['text']

    def get_membership(self,mem_id):
        def buildUrl():
            return self.url+'memberships/'+str(mem_id)
        resp=requests.get(buildUrl(),headers=self.headers)
        if resp.status_code >= 300:
            print("Error in the api")
            print(resp.status_code)
            resp.raise_for_status()
        else:
            if resp.json() is not None:
                return resp.json()['personEmail']

    def send_message(self,input,receiver):
        message=input['message']
        return self.send_message_orig(message,room_id=receiver)

    def send_message_orig(self,message,room_id=None,person_id=None):
        def buildUrl():
            return self.url+'messages'
        def buildJson():
            if room_id:
                return {
                    "roomId":room_id,
                    "markdown":message
                }
            elif person_id:
                return{
                    "toPersonId":person_id,
                    "markdown":message
                }
        resp=requests.post(buildUrl(),json=buildJson(),headers=self.headers)
        if resp.status_code >= 300:
            print("Error in the api")
            print(resp.status_code)
            resp.raise_for_status()
        else:
            return True

