#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 1:10 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : keywords.py
# @Software: PyCharm

# Just a dummy file for the demo (keywords)
# Action List


###We need to implement the tense form transformation

GREETINGS = {'hello': {'UH': ['hi', 'hello']}, 'goodbye': {'UH': ['goodbye']},
             'say_welcome': {'NNS': ['thanks', 'thank']}}
ACTIONS = {'add_space': {'OR': {'VB': ['add', 'provision', 'have', 'get', 'increase', 'want', 'like', 'need','give'],
                                'JJR': ['more']},
                         'NN': ['space', 'gb', 'disk', 'size', 'storage']},
           'say_welcome': {'VBP': ['thanks', 'thank']},
           'no_space': {'OR':{'VBD': ['blew'],'IN':['out'],'JJ':['low']}, 'NN': ['directory', 'space', 'disk', 'server']}}

NOUNS = {'say_welcome': {'NNS': ['thanks', 'thank']}, 'ask_time': {'WP': ['what'], 'NN': ['time']}}
QUERYS = {'ask_time': {'WRB': ['how'], 'RB': ['long']}}
KEYWORDS = {"GREETINGS": GREETINGS, "ACTIONS": ACTIONS, 'NOUNS': NOUNS, "QUERYS": QUERYS}

# To identify whether it's a service:



server = {
    'result': [{
        'filter': 'dep',
        'name': 'pobj',
        'regex': [r'\S+-\S+', r'\S+\.\S+']
    },
        {
            'filter': 'dep',
            'name': 'conj',
            'regex': [r'\S+-\S+', r'\S+\.\S+']
        },
        {
            'filter': 'dep',
            'name': 'obj',
            'regex': [r'\S+-\S+', r'\S+\.\S+']
        },
        # Some times it goes direct to the root.
        {
            'filter': 'dep',
            'name': 'root',
            'regex': [r'\S+-\S+', r'\S+\.\S+']
        }
    ],
    # This is for the pos_tag match rule
    'pos_tag': {'OR': {'NN': ['server', 'host', 'hostname'], 'VB': ['provision', 'use','server'],
                       'IN': ['on', 'at', 'in', 'under', 'to']}},
    # This is for the dep match rule
    'dep': {}
}
space = {
    'result': [{
        'filter': 'dep',
        'name': 'pobj',
        'regex': r'\d+[a-zA-z]+'
    },
        {
            'filter': 'dep',
            'name': 'conj',
            'regex': r'\d+[a-zA-z]+'
        },
        {
            'filter': 'dep',
            'name': 'dobj',
            'regex': r'\d+[a-zA-z]+'
        },
        # Some times it goes direct to the root.
        {
            'filter': 'dep',
            'name': 'root',
            'regex': '\d+[a-zA-z]+'
        }
    ],
    # This is for the pos_tag match rule
    'pos_tag': {
        'OR': {'NN': ['path', 'space'], 'VB': ['need', 'want', 'add', 'provision'], 'IN': ['on', 'at', 'in', 'under']}},
    # This is for the dep match rule
    'dep': {}
}
path = {
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
            'name': 'root',
            'regex': r'/\S'
        },
        {
            'filter': 'brute_force',
            'regex': r'/\S'
        }
    ],
    # This is for the pos_tag match rule
    'pos_tag': {'OR': {'NN': ['path', 'location', 'place'], 'VB': ['provision'], 'IN': ['on', 'at', 'in', 'under']}},
    # This is for the dep match rule
    'dep': {}
}
ADD_SPACE = {'server_name': server,
             'space_size': space,
             'path': path
             }

EXPECT_LIST = {'add_space': ADD_SPACE}
