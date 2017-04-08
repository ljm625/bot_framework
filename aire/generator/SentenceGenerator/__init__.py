#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 11:52 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : sentenceGenerator.py
# @Software: PyCharm

from PhrasesPicker import PhrasePicker
from aire.generator.GeneratorAbstract import GeneratorAbstract


class SentenceGenerator(GeneratorAbstract):
    def __init__(self):
        pass

    @classmethod
    def get_instance(cls, input=None):
        return cls()

    def greetings(self):
        # This is used to generate the greetings
        pass

    def generate(self, input):
        action = input['action']
        phasepicker = PhrasePicker()
        if action in phasepicker.actions:
            return phasepicker.get_phrase(action)
        elif action == 'say_welcome':
            return "You're welcome, it's my pleasure to help ;)"
        elif action == 'ask_time':
            return "I think it will take approximately **5 minute**."
        elif action == 'no_space':
            return ["Running out of **space**? You came to the right bot :D I can definately help on that!",
                    "I need to get the **server name**, the **size** you want to add and the **path** to increase in order to help."]
        else:
            return phasepicker.get_phrase('not_sure')

    def generate_param_request(self, params):
        base_sentence = 'I still need '
        end_sentence = ' in order to process this service.'
        mid_sentence = ''
        for param in params:
            if not mid_sentence:
                mid_sentence = mid_sentence + param
            else:
                mid_sentence = mid_sentence + ', ' + param
        return base_sentence + mid_sentence + end_sentence

    def generate_service_review(self, params):
        base_sentence = "Okay, so far I knew that "
        mid_sentence = ''
        for k, v in params.items():
            if not mid_sentence:
                mid_sentence = mid_sentence + k + ' is set to ' + v
            else:
                mid_sentence = mid_sentence + ' and ' + k + ' is set to ' + v
        return base_sentence + mid_sentence
