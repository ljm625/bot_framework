#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 11:32 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from pprint import pprint

from mainParser import MainParser
from syntaxNetParse import SyntaxParser

if __name__ == '__main__':
    synparser=SyntaxParser()
    sentence="I'd like to add more space on server XYZ.CISCO.COM."
    result=synparser.parse_sentence([sentence])
    pprint(result)
    pos_tag,dep=synparser.tokenize(result[0])
    print(pos_tag)
    print(dep)
    parser=MainParser(sentence)
    print parser.make_category()
    # parser.check_action('GREETINGS','123')