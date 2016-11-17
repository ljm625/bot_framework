# this file is for working on chunking of the words together
## adapted from nltk tutuorials

import nltk
from nltk.corpus import stopwords as sw


def process_sentence(json_sentence, wordlist):
    try:
        for i in json_sentence:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            wordlist.append(words)
    except Exception as e:
        print(str(e))

def chunk_sentence(json_sentence):
    try:
        for i in json_sentence:
            words = nltk.word_tokenize(i)
            print words
            tagged = nltk.pos_tag(words)
            chunk_gram = r"""Chunked: {<RB.>*<VB.?>*<NNP>+<NN>?} """

            ## what is the storage capacity of filer a?
            ## automate the creation of the chunk rules over time

            chunk_parser = nltk.RegexpParser(chunk_gram)
            chunked = chunk_parser.parse(tagged)
            print chunked
    except Exception as e:
        print(str(e))