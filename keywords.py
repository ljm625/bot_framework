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

# To identify whether it's a service:



server={
    'result':[{
        'filter':'dep',
        'name':'pobj',
        'regex':[r'\S+-\S+',r'\S+\.\S+']
    },
    {
        'filter': 'dep',
        'name': 'conj',
        'regex': [r'\S+-\S+',r'\S+\.\S+']
    },
        # Some times it goes direct to the root.
        {
        'filter':'dep',
        'name':'ROOT',
        'regex':[r'\S+-\S+',r'\S+\.\S+']
        }
    ],
    #This is for the pos_tag match rule
    'pos_tag':{'OR':{'NN':['server','host','hostname'],'VB':['provision','use'], 'IN':['on','at','in','under','to']}},
    # This is for the dep match rule
    'dep':{}
}
space={
    'result': [{
        'filter': 'dep',
        'name': 'pobj',
        'regex': ''
    },
    {
        'filter': 'dep',
        'name': 'conj',
        'regex': r'/\S'
    },
        # Some times it goes direct to the root.
        {
            'filter': 'dep',
            'name': 'ROOT',
            'regex': ''
        }
    ],
    # This is for the pos_tag match rule
    'pos_tag': {'OR': {'NN':['path','location','place'],'VB':['provision'], 'IN':['on','at','in','under']}},
    # This is for the dep match rule
    'dep': {}
}
path={
    'result': [{
        'filter': 'dep',
        'name': 'pobj',
        'regex': r'/\S'
    },
    {
        'filter': 'dep',
        'name': 'conj',
        'regex': r'/\S'
    },
        # Some times it goes direct to the root.
        {
            'filter': 'dep',
            'name': 'ROOT',
            'regex': r'/\S'
        }
    ],
    # This is for the pos_tag match rule
    'pos_tag': {'OR': {'NN':['path','location','place'],'VB':['provision'], 'IN':['on','at','in','under']}},
    # This is for the dep match rule
    'dep': {}
}
ADD_SPACE={'server_name':server,
           # 'space_size':space,
           'path':path
           }




EXPECT_LIST={'add_space':ADD_SPACE}
