#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/2016 11:43 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : expectParser.py
# @Software: PyCharm


# So basically this file is for continuous logic, we expect the missing parameters from the user

server={}
space={}
path={}
ADD_SPACE={'server_name':server,
           'space_size':space,
           'path':path}

class ExpectParser(object):
    def __init__(self,service_name,session):
        self.service_name=service_name
        self.session=session
        pass

    def expect(self):
        pass

