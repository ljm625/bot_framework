#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/2016 11:32 AM
# @Author  : Jiaming Li  (jiaminli@cisco.com)
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from pprint import pprint

from sentenceGenerator import SentenceGenerator
from expectParser import ExpectParser
from keywords import EXPECT_LIST
from mainParser import MainParser
from sparkAPI import SparkAPI
from syntaxNetParse import SyntaxParser

if __name__ == '__main__':
    # synparser=SyntaxParser()
    # sentence="the server is XYZ.CISCO.COM and the path is /root"
    # result=synparser.parse_sentence([sentence])
    # pprint(result)
    # pos_tag,dep=synparser.tokenize(result[0])
    # print(pos_tag)
    # print(dep)
    # parser=MainParser(sentence)
    # action=parser.make_category()
    # if action in EXPECT_LIST:
    #     expect=ExpectParser('etst','123','add_space')
    #     expect.parse(result)
    #     expect.expect_params()
    # else:
    #     generator= SentenceGenerator()
    #     print generator.generate(action)
    # parser.check_action('GREETINGS','123')
    spark=SparkAPI()
    spark.send_message('hehehehe','Y2lzY29zcGFyazovL3VzL1JPT00vYTUxZGZhMTAtYmNiMC0xMWU2LWJhZTYtZGRkZGEzMDYxNGRm')