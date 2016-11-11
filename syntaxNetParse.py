# Author: joshwong@cisco.com
# Purpose: interface for the pos_tagger for the NLP/ML

import requests
import json

### REQUIRES THE SYNTAXNET LOCAL DOCKER IMAGE ### ask Jiaming for details

def sentenceInput(sentence):

    url = "http://localhost:9000/api/v1/query"
    payload = "{\n   \"strings\": [\"%s\"]\n}" % sentence
    headers = {
        'authorization': "Basic YWRtaW5pc3RyYXRvcjphZG1pbmlzdHJhdG9y",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "4ee89f2a-8cc5-0ae9-40ea-fb5f7c8a7ad3"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    sentenceParse = json.loads(response.text)
    return sentenceParse




