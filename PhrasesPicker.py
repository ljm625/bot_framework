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
        pass

    def get_phrase(self,action):
        random.seed(datetime.now())
        phrase_obj=Phrases()
        phrases = phrase_obj.get(action)
        num=random.randint(0, len(phrases) - 1)
        print num
        print phrases[num]
        return phrases[num]