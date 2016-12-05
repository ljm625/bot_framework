#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 11:52 AM
# @Author  : Zach Antonas  (zantonas@cisco.com)
# @Site    : 
# @File    : Phrases.py
# @Software: PyCharm

import random
from datetime import datetime
from Phrases import Phrases

# Returns a random phrase from a list of phrases.
class PhrasePicker(str):

    actions = ['hello', 'no_problem', 'goodbye', 'not_sure']

    def __init___(self,action):
        self = self.__get_phrase__(action)

    def __get_phrase__(self,action):
        random.seed(datetime.now())
        phrases = Phrases.get(action)
        return phrases[random.randint(0, len(phrases) - 1)]