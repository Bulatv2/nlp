# class Words

from tokenize import Tokenize
import re

class Words(Tokenize):
    """ делает токинезацию по словам """
    wordslist = []
    getstring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по словам """
        self.getstring = Tokenize.load(self)
        self.wordslist = re.split("(\w+|[a-z])", self.getstring)
        print(self.wordslist)
        return self.wordslist
