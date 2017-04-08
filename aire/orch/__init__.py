# This file is the core of the bot engine
import re
from pprint import pprint

import yaml

from aire import config
from aire.action_parser.ActionClassifier import ActionClassifier
from aire.action_parser.ExpectParser import ExpectParser
from aire.generator.SentenceGenerator import SentenceGenerator
from aire.keywords import EXPECT_LIST
from aire.messenger.Spark import Spark
from aire.nlp.SyntaxnetParser import SyntaxnetParser

"""
TODO:

Use the component here instead of hard code!

"""

EXPECT_OBJECTS=[]

class Orch(object):
    def __init__(self):
        pass

    def yaml_reader(self,yaml_file):
        with open(yaml_file, 'r') as file:
            dict = yaml.load(file)
            return dict

    def read_configuration(self,yaml_file):
        config=self.yaml_reader(yaml_file)
        return config


    def message_parse(self,args):
        msg_id = args['data']['id']
        room_id = args['data']['roomId']
        print(room_id)
        person_id = args['data']['personId']
        person_email = args['data']['personEmail']
        time = args['data']['created']
        # Now we need to retrieve this message.
        if person_email == config.BOT_ACCOUNT:
            # I don't want to receive infinite messages lol
            return 204

        spark = Spark.get_instance()
        message = spark.get_message({'msg_id':msg_id})

        # Remove the BOT Name from the sentence.
        if config.BOT_NAME in message:
            message = message.replace(config.BOT_NAME, '')
        message.strip(' ')
        message = re.sub(' +', ' ', message)

        synparser = SyntaxnetParser.get_instance()
        result = synparser.parse_sentence([message])[0]
        pprint(result)
        #pos_tag, dep = synparser.tokenize(result[0])
        #print(pos_tag)
        #print(dep)
        generator = SentenceGenerator.get_instance()


        # Here try to use factory method to get expect class
        expect_instance=ExpectParser.get_instance({'session':room_id})

        if expect_instance:
            all_done, params = expect_instance.parse_input({"sentence": message, "parsed_sentence": result})
            if all_done:
                # All done
                reply = []
                reply.append(generator.generate_service_review(params))
                reply.append("I will start to execute the service for you. Please wait a few minutes.")
                ExpectParser.del_instance({'session':room_id})
            else:
                reply = []
                reply.append(generator.generate_service_review(expect_instance.get_params()))
                reply.append(generator.generate_param_request(params))
        else:
            parser = ActionClassifier.get_instance({'sentence':message,'parsed_sentence':result})
            action = parser.make_category()
            if action in EXPECT_LIST:
                expect = ExpectParser.get_instance({"session":room_id,"expect_name":action})
                reply = []
                reply.append('Sure I can definitely help you on that :D')
                all_done,params=expect.parse_input({"sentence": message, "parsed_sentence": result})
                if not all_done:
                    reply.append(generator.generate_param_request(params))
            else:
                reply = generator.generate({"action":action})
        if type(reply) == list:
            for msg in reply:
                spark.send_message({"message":msg}, room_id)
        elif type(reply) == str or type(reply) == unicode:
            spark.send_message({"message":reply}, room_id)