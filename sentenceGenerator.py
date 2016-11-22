#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 11:52 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : sentenceGenerator.py
# @Software: PyCharm


class SentenceGenerator(object):
    def __init__(self):
        pass

    def greetings(self):
        # This is used to generate the greetings
        pass

    def generate(self,action):
        if action=='say_hello':
            return "Hello from the BOT :D What can I do for you?"
        elif action=='say_welcome':
            return "You're welcome, it's my pleasure to help ;)"
        elif action=='ask_time':
            return "I think it will take approximately 5 minute."
        elif action=='no_space':
            return ["Running out of space? You came to the right bot :D I can definately help on that!",
                    "I need to get the server name, the size you want to add and the path to increase in order to help."]
