#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 1:10 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : keywords.py
# @Software: PyCharm

# Just a dummy file for the demo (keywords)
#Action List


###We need to implement the tense form transformation

GREETINGS={'say_hello':{'UH':['hi','hello']},'say_goodbye':{'UH':['goodbye']}}
ACTIONS={'add_space':{'VB':['add','provision','have','get','increase','want','like','need'],
                      # 'JJR':['more'],
                      'NN':['space','gb','disk','size']},
         'say_welcome': {'VBP': ['thanks', 'thank']},
         'no_space':{'VBD':['blew'],'NN':['directory','space','disk','server']}}

NOUNS={'say_welcome': {'NNS': ['thanks', 'thank']},'ask_time':{'WP':['what'],'NN':['time']}}
QUERYS={'ask_time':{'WRB':['how'],'RB':['long']}}
KEYWORDS={"GREETINGS":GREETINGS,"ACTIONS":ACTIONS,'NOUNS':NOUNS,"QUERYS":QUERYS}

