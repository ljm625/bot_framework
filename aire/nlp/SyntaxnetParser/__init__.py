#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 1:30 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : depParser.py
# @Software: PyCharm

import requests

from aire.config import SYNTAXNET_IP
from aire.nlp.NlpAbstract import NlpAbstract

class SyntaxnetParser(NlpAbstract):
    instance_list = {}
    def __init__(self,url,language):
        self.url=url+'/api/v1/query'
        self.headers={'content-type': "application/json"}
        requests.get("{}/api/v1/use/{}".format(url,language), headers=self.headers)

    @classmethod
    def get_instance(cls, input=None):
        # Single instance Mode
        url=SYNTAXNET_IP
        language='English'
        if(input):
            assert type(input)==dict
            if(input.get("url")): url=input.get("url")
            if(input.get("language")): language=input.get("language")
        if (cls.instance_list.get(language)):
            return cls.instance_list.get(language)
        else:
            cls.instance_list[language]=cls(url,language)
            return cls.instance_list[language]


    def parse_sentence(self,sentences):
        # For accurate purpose, the first one should be lowercase.
        new_sentence_list=[]
        for sentence in sentences:
            sentence=sentence.strip(' ')
            new_sentence=sentence[0].lower()+sentence[1:]
            if sentence[-1] not in ['.', '?', '!', '~',',']:
                new_sentence=new_sentence+'.'
            new_sentence_list.append(new_sentence)
        response = requests.post(self.url, json={"strings":new_sentence_list,"tree":True}, headers=self.headers)
        return response.json()







