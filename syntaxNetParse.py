# Author: joshwong@cisco.com
# Purpose: interface for the pos_tagger for the NLP/ML

import requests
import json

### REQUIRES THE SYNTAXNET LOCAL DOCKER IMAGE ### ask Jiaming for details


class SyntaxParser(object):
    def __init__(self,url='http://localhost:9000'):
        self.url=url+'/api/v1/query'
        self.headers={'content-type': "application/json"}

    def parse_sentence(self,sentences):
        # For accurate purpose, the first one should be lowercase.
        new_sentence_list=[]
        for sentence in sentences:
            sentence=sentence.strip(' ')
            new_sentence=sentence[0].lower()+sentence[1:]
            if sentence[-1] not in ['.', '?', '!', '~',',']:
                new_sentence=new_sentence+'.'
            new_sentence_list.append(new_sentence)
        response = requests.post(self.url, json={"strings":new_sentence_list}, headers=self.headers)
        return response.json()

    def tokenize(self,parsed_sentence):
        # This function is used to change it into the token pair for result querying.
        pos_tag={}
        dep={}
        def generate_token(obj):
            if obj:
                if obj['pos_tag'] in pos_tag:
                    pos_tag[obj['pos_tag']].append(obj['name'])
                else:
                    pos_tag[obj['pos_tag']]=[obj['name']]
                if obj['dep'] in dep:
                    dep[obj['dep']].append(obj['name'])
                else:
                    dep[obj['dep']]=[obj['name']]
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
        return pos_tag,dep






