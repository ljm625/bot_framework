#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 1:30 PM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : depParser.py
# @Software: PyCharm

class DepParser(object):
    def __init__(self,dep):
        self.dep=dep

    def get_root(self):
        return self.dep['ROOT'][0]