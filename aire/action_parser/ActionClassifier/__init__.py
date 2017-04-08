#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 1:55 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : mainParser.py
# @Software: PyCharm

# This file is mainly used in parse the sentence
from aire.action_parser.ActionAbstract import ActionAbstract
from aire.keywords import *


class ActionClassifier(ActionAbstract):
    def __init__(self,sentence,parsed_result):
        #self.synparser = SyntaxParser()
        self.result = parsed_result
        self.sentence=sentence
        self.pos_tag,self.label=self.tokenize(parsed_result)
        #self.depParser=DepParser(self.dep)
        #self.posParser=PosTagParser(self.pos_tag)

    @classmethod
    def get_instance(cls,input):
        assert type(input)==dict
        if(input.get('sentence') and input.get('parsed_sentence')):
            return cls(sentence=input.get('sentence'),parsed_result=input.get('parsed_sentence'))
        else: return None

    def parse_input(self,input):
        return self.make_category()

    def get_root(self):
        root=self.label['root'][0]
        for j,k in self.pos_tag.items():
            for ele in k:
                if ele==root:
                    return root,j
        return root,None

    def make_category(self,input=None):
        def deep_loop(cur_stuff):
            if 'contains' in cur_stuff:
                cat = self.make_category(cur_stuff)
                if cat != 'Unknown':
                    return cat
            return 'Unknown'
        if not input:
            input=self.result
        tag=input['pos_tag']
        pos_tag,dep=self.tokenize(input)
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
            return 'Unknown'
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
            return 'Unknown'
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
            return 'Unknown'
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
        pos_tag,dep=self.tokenize(input)
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
        # Update : Enable the function of OR here.
        for option,info in CatInfo.items():
            root, root_tag = self.get_root()
            check_list=self.build_precheck(info)
            if (stuff['pos_tag'] in check_list and stuff['word'].lower() in check_list[stuff['pos_tag']])\
                    or (root_tag in check_list and root.lower() in check_list[root_tag]):
                # We can continue.
                pos_tag=self.get_postag(stuff)
                result=self.loop_check(info,pos_tag)
                if result:
                    return option
        return 'Unknown'

    def build_precheck(self,cat_info):
        result={}
        for k,v in cat_info.items():
            if type(v)==dict:
                for k1,v1 in v.items():
                    if k1 in result:
                        result[k1].extend(v1)
                    else:
                        result[k1]=v1
            else:
                if k in result:
                    result[k].extend(v)
                else:
                    result[k] = v
        return result


    def loop_check(self,cur_info,pos_tag):
        try:
            for k, v in cur_info.items():
                if type(v)==dict:
                    match = False
                    for k1, v1 in v.items():
                        if match:
                            break
                        if k1 in pos_tag:
                            for stuff in pos_tag[k1]:
                                if stuff in v1:
                                    match = True
                                    break
                    if not match:
                        return False
                else:
                    match = False
                    for stuff in pos_tag[k]:
                        if stuff.lower() in v:
                            match = True
                            break
                    if not match:
                        return False
            return True
        except Exception as e:
            return False

    def tokenize(self,parsed_sentence):
        # This function is used to change it into the token pair for result querying.
        pos_tag={}
        label={}
        def generate_token(obj):
            if obj:
                if obj['pos_tag'] in pos_tag:
                    pos_tag[obj['pos_tag']].append(obj['word'])
                else:
                    pos_tag[obj['pos_tag']]=[obj['word']]
                if obj['label'] in label:
                    label[obj['label']].append(obj['word'])
                else:
                    label[obj['label']]=[obj['word']]
            return obj
        def loop_sentence(objs):
            if type(objs)==list:
                for obj in objs:
                    if 'contains' in obj:
                        loop_sentence(obj['contains'])
                    generate_token(obj)
            else:
                if 'contains' in objs:
                    loop_sentence(objs['contains'])
                generate_token(objs)

        loop_sentence(parsed_sentence)
        return pos_tag,label