from aire import config
from aire.typo_fix.TypoAbstract import TypoAbstract
from enchant.checker import SpellChecker

class EnchantParser(TypoAbstract):
    def __init__(self,language=config.LANGUAGE):
        self.checker = SpellChecker(language)

    @classmethod
    def get_instance(cls, input):
        return cls()

    def parse_input(self,input):
        ''' This function automatically replace the wrong word with the dict.'''
        sentence=input['sentence']
        self.checker.set_text(sentence)
        for err in self.checker:
            errword=err.word
            sug = err.suggest()[0]
            print("Change:{} to {}".format(errword,sug))
            err.replace(sug)
        return self.checker.get_text()
