#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 1:55 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : mainParser.py
# @Software: PyCharm

# This file is mainly used in parse the sentence
from keywords import *
from depParser import DepParser
from postagParser import PosTagParser

from syntaxNetParse import SyntaxParser


class MainParser(object):
    def __init__(self,sentence):
        self.synparser = SyntaxParser()
        self.result = self.synparser.parse_sentence([sentence])[0]
        self.sentence=sentence
        self.pos_tag,self.dep=self.synparser.tokenize(self.result)
        self.depParser=DepParser(self.dep)
        self.posParser=PosTagParser(self.pos_tag)

    def get_root(self):
        root=self.depParser.get_root()
        tag=self.posParser.find_word_tag(root)
        return root,tag

    def make_category(self,input=None):
        def deep_loop(cur_stuff):
            if 'contains' in cur_stuff:
                if 'contains' in cur_stuff:
                    cat = self.make_category(cur_stuff)
                    if cat != 'Unknown':
                        return cat
                return 'Unknown'
            return 'Unknown'
        if not input:
            input=self.result
        tag=input['pos_tag']
        pos_tag,dep=self.synparser.tokenize(input)
        if tag=='UH' or tag=='NNS':
            # This should be a greeting
            if 'contains' in input:
                for stuff in input['contains']:
                    result=self.check_action('GREETINGS',stuff)
                    if result!='Unknown':
                        return result
                    else:
                        result = deep_loop(stuff)
                        if result != 'Unknown':
                            return result
            return 'GREETINGS'
        elif 'VB' in tag:
            # Need to do something
            # Try to check whether it is suitable for this category
            if 'contains' in input:
                for stuff in input['contains']:
                    result=self.check_action('ACTIONS',stuff)
                    if result!='Unknown':
                        return result
                    else:
                        result = deep_loop(stuff)
                        if result != 'Unknown':
                            return result
            return 'ACTIONS'
        elif 'NN' in tag:
            if 'contains' in input:
                for stuff in input['contains']:
                    result = self.check_action('NOUNS', stuff)
                    if result != 'Unknown':
                        return result
                    else:
                        result=deep_loop(stuff)
                        if result!='Unknown':
                            return result
            return 'Name'
        # elif tag=='NN':
        else:
            if 'WRB' in pos_tag and str(pos_tag['WRB'][0]).lower()=='how':
                result = self.check_action('QUERYS', input)
                if result != 'Unknown':
                    return result
                # TODO: FIX
                else:
                    return 'Unknown'
            else:
                if 'contains' in input:
                    for stuff in input['contains']:
                        result = deep_loop(stuff)
                        if result != 'Unknown':
                            return result
                else:
                    return 'Unknown'

    def get_postag(self,input):
        pos_tag,dep=self.synparser.tokenize(input)
        root, tag = self.get_root()
        if tag in pos_tag:
            pos_tag[tag].append(root)
        else:
            pos_tag[tag]=[root]
        return pos_tag
        # We added the Root in the content, now we can do a regex

    def check_action(self,category,stuff):
        CatInfo=KEYWORDS[category]
        # exec 'CatInfo='+category
        for option,info in CatInfo.items():
            root,root_tag = self.get_root()
            if (stuff['pos_tag'] in info and stuff['name'].lower() in info[stuff['pos_tag']])\
                    or (root_tag in info and root.lower() in info[root_tag]):
                # We can continue.
                pos_tag=self.get_postag(stuff)
                result=self.loop_check(info,pos_tag)
                if result:
                    return option
        return 'Unknown'

    def loop_check(self,cur_info,pos_tag):
        try:
            for k, v in cur_info.items():
                match = False
                for stuff in pos_tag[k]:
                    if stuff.lower() in v:
                        match = True
                        break
                if not match:
                    return False
            return True
        except Exception, e:
            return False