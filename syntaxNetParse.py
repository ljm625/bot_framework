# Author: joshwong@cisco.com
# Purpose: interface for the pos_tagger for the NLP/ML

import requests
import json

### REQUIRES THE SYNTAXNET LOCAL DOCKER IMAGE ### ask Jiaming for details

def sentenceInput(sentence):

    url = "http://localhost:9000/api/v1/query"
    payload = "{\n   \"strings\": [\"%s\"]\n}" % sentence
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    sentenceParse = json.loads(response.text)
    return sentenceParse




