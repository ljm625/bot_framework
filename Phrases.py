#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/03/2016 21:52 PM
# @Author  : Zach Antonas  (zantonas@cisco.com)
# @Site    : 
# @File    : Phrases.py
# @Software: PyCharm

import random
from datetime import datetime

class Phrases:

    def get(self,action):
        if action == 'hello':
            return self.hello()
        elif action == 'no_problem':
            return self.no_problem()
        elif action == 'goodbye':
            return self.goodbye()
        else: # not_sure
            return self.not_sure()

    # Return random hello phrase
    def hello(self):
        hello = [
                "Hello my name is GimmeBot, how can I help you?",
                "Hi this is GimmeBot, how can I help?",
                "Hi i'm GimmeBot, what can I help you with?",
                "Hello, how may I help you?",
                "Hi! My name is GimmeBot, can I help with something?",
                "GimmeBot at your service! How may I serve you?",
                "Hello, how can I help you?",
                "GimmeBot has arrived! What can I help you with?",
                "Greetings! What can I do for you?",
                "Greetings! This is GimmeBot, how can I help?"
                ]
        return hello

    def no_problem(self):
        no_problem = [
            "You're welcome.",
            "You're very welcome!"
            "No problem.",
            "No problem at all!",
            "This was no problem for GimmeBot!",
            "Not a problem.",
            "You are welcome."
        ]
        return no_problem

    def goodbye(self):
        goodbye = [
                'Goodbye!',
                'Bye for now!',
                'Goodbye, GimmeBot over and out!',
                'Bye!',
                'Goodbye, see you soon!'
                ]
        return goodbye

    def not_sure(self):
        dead_end = [
                "Sorry I don't understand the question... can you phrase your sentence differently?",
                "I don't understand.",
                "I'm not sure what you mean.",
                "I'm not sure what you're trying to say.",
                "I'm confused... what do you mean?",
                "Im not sure what you mean by that.",
                "Erm... I don't understand.",
                "Sorry, I don't understand what you're saying.",
                "Sorry, I'm not sure what you mean.",
                "Sorry, I'm not sure what you're trying to say."
                ]
        return dead_end
