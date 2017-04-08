#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 11:43 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    :
# @File    : expectParser.py
# @Software: PyCharm


# So basically this file is for continuous logic, we expect the missing parameters from the user

#

# The server name is always in pobj in dep
import re

from aire.action_parser.ActionAbstract import ActionAbstract
from aire.keywords import EXPECT_LIST


class ExpectParser(ActionAbstract):
    instance_list={}
    def __init__(self,session,expect_name,expect_list=EXPECT_LIST):
        self.session=session
        self.params={}
        #self.synparser = SyntaxParser()
        self.expect=expect_list.get(expect_name)
        if not self.expect:
            raise NameError("The expect_name is not defined!")

    @classmethod
    def get_instance(cls,input):
        """Single instance mode"""
        assert type(input)==dict
        expect_list=EXPECT_LIST
        if(not input.get('session')): return None
        if(input.get('expect_list')): expect_list=input.get('expect_list')
        if(cls.instance_list.get(input['session'])):
            return cls.instance_list.get(input['session'])
        else:
            if(input.get('expect_name')):
                tmp_obj=cls(session=input['session'],expect_name=input['expect_name'],expect_list=expect_list)
                cls.instance_list[input['session']]=tmp_obj
                return tmp_obj
            else: return None

    @classmethod
    def del_instance(cls,input):
        assert type(input) == dict
        if (not input.get('session')): return None
        if (cls.instance_list.pop(input['session']),None):
            return True
        return None

    def parse_input(self,input):
        ''' Parse the input and check if all the requirements are fullfilled'''
        assert type(input)==dict
        if(input.get('sentence') and input.get('parsed_sentence')):
            self.parse(input['sentence'],input['parsed_sentence'])
        if self.expect_params():
            return False,self.expect_params()
        else:
            return True,self.get_params()


    def expect_parser(self,rules,s_pos,s_dep):
        def analyze(analyze_type):
            # Just go deeper and analyze
            if analyze_type=='pos_tag':
                for k,v in pos_tag.items():
                    if type(v)==dict:
                        match=False
                        for k1,v1 in v.items():
                            if match:
                                break
                            if k1 in s_pos:
                                for stuff in s_pos[k1]:
                                    if stuff in v1:
                                        match=True
                                        break
                        if not match:
                            return False
                    else:
                        for stuff in s_pos[k]:
                            if stuff not in v:
                                return False
                return True
            elif analyze_type == 'dep':
                for k, v in dep.items():
                    if type(v) == dict:
                        match = False
                        for k1, v1 in v.items():
                            if match:
                                break
                            if k1 in s_dep:
                                for stuff in s_dep[k1]:
                                    if stuff in v1:
                                        match = True
                                        break
                        if not match:
                            return False
                    else:
                        for stuff in s_dep[k]:
                            if stuff not in v:
                                return False
                return True
        pos_tag = rules['pos_tag']
        dep = rules['dep']
        match=True
        if pos_tag:
            if not analyze('pos_tag'):
                match=False
        if dep:
            if not analyze('dep'):
                match=False
        return match

    def get_token(self, input,root,root_tag,root_dep):
        pos_tag, dep = self.tokenize(input)

        if root_tag in pos_tag:
            pos_tag[root_tag].append(root)
        else:
            pos_tag[root_tag] = [root]
        if root_dep in dep:
            dep[root_dep].append(root)
        else:
            dep[root_dep] = [root]
        return pos_tag,dep

    def parse(self,sentence,parsed_sentence):
        # Here We need to use a seperate engine for analyze.
        # Check what we have now.

        # Update, the need to support BRUTE FORCE since some of the keywords will be break by nlp engine
        def formatter():
            return sentence.split(' ')

        word_list=formatter()


        def update_params(param,value):
            self.params[param]=value
        for k,v in self.expect.items():
            if self.params.get(k):
                # The param is already exist.
                pass
            else:
                if 'contains' in parsed_sentence:
                    root_tag=parsed_sentence['pos_tag']
                    root_dep=parsed_sentence['label']
                    root=parsed_sentence['word']
                    for stuff in parsed_sentence['contains']:
                        tag,dep=self.get_token(stuff,root,root_tag,root_dep)
                        if self.expect_parser(v,tag,dep):
                            result = self.get_result(v['result'], parsed_sentence,word_list)
                            if result:
                                update_params(k, result)
                else:
                    tag,dep=self.tokenize(parsed_sentence)
                    if self.expect_parser(v, tag, dep):
                        result=self.get_result(v['result'], parsed_sentence,word_list)
                        if result:
                            update_params(k,result)


    def get_result(self,result_rule,parsed_sentence,word_list):
        pos_tag,dep=self.tokenize(parsed_sentence)
        for stuff in result_rule:
            if stuff['filter']=='pos_tag':
                if stuff['name'] in pos_tag:
                    if type(stuff['regex'])==list:
                        for regex in stuff['regex']:
                            pattern=re.compile(regex)
                            for data in pos_tag[stuff['name']]:
                                match = pattern.match(data)
                                if match:
                                    return data
                    else:
                        pattern=re.compile(stuff['regex'])
                        for data in pos_tag[stuff['word']]:
                            match=pattern.match(data)
                            if match:
                                return data
            elif stuff['filter']=='dep':
                if stuff['name'] in dep:
                    if type(stuff['regex']) == list:
                        for regex in stuff['regex']:
                            pattern = re.compile(regex)
                            for data in dep[stuff['name']]:
                                match = pattern.match(data)
                                if match:
                                    return data
                    else:
                        pattern = re.compile(stuff['regex'])
                        for data in dep[stuff['name']]:
                            match = pattern.match(data)
                            if match:
                                return data
            elif stuff['filter']=='brute_force':
                if type(stuff['regex']) == list:
                    for regex in stuff['regex']:
                        pattern = re.compile(regex)
                        for data in word_list:
                            match = pattern.match(data)
                            if match:
                                return data
                else:
                    pattern = re.compile(stuff['regex'])
                    for data in word_list:
                        match = pattern.match(data)
                        if match:
                            return data
        return None

    def check_status(self):
        ''' This method is only for debug purpose '''
        for k, v in self.expect.items():
            if self.params.get(k):
                # The param is already exist.
                print("got param {} {}".format(str(k),self.params[k]))
            else:
                print("waiting for param {}".format(str(k)))

    def get_session(self):
        return self.session

    def get_params(self):
        return self.params
    def expect_params(self):
        expect_list=[]
        for k, v in self.expect.items():
            if self.params.get(k):
                pass
            else:
                expect_list.append(k)
        return expect_list

    def tokenize(self, parsed_sentence):
        # This function is used to change it into the token pair for result querying.
        pos_tag = {}
        label = {}

        def generate_token(obj):
            if obj:
                if obj['pos_tag'] in pos_tag:
                    pos_tag[obj['pos_tag']].append(obj['word'])
                else:
                    pos_tag[obj['pos_tag']] = [obj['word']]
                if obj['label'] in label:
                    label[obj['label']].append(obj['word'])
                else:
                    label[obj['label']] = [obj['word']]
            return obj

        def loop_sentence(objs):
            if type(objs) == list:
                for obj in objs:
                    if 'contains' in obj:
                        loop_sentence(obj['contains'])
                    generate_token(obj)
            else:
                if 'contains' in objs:
                    loop_sentence(objs['contains'])
                generate_token(objs)

        loop_sentence(parsed_sentence)
        return pos_tag, label