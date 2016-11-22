#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 11:50 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : postagParser.py
# @Software: PyCharm


class PosTagParser(object):
    def __init__(self,pos_tag):
        self.postag=pos_tag
        pass

    def find_word_tag(self,word):
        for k,v in self.postag.items():
            if word in v:
                return k
        return None

    def parse_ut(self):
        # This part is mainly for greetings.
        if 'UT' in self.postag:
            return True
        else: return False