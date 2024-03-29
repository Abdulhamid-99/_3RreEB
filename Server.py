from nltk import CoreNLPParser

class _3RreEB(object):
    def __init__(self, Path, State):
        self.__Path = Path
        self.__State = State
        match self.__State:
            case 0:
                self.__stf_parser = CoreNLPParser(self.__Path)
            case 1:
                self.__stf_parser = CoreNLPParser(self.__Path, tagtype='pos')
            case default:
                self.__stf_parser = CoreNLPParser(self.__Path)

    def Parse(self, text):
        if self.__State == 0:
            self.__text = text
            return list(self.__stf_parser.raw_parse(text))
        else:
            return "Wrong Mode"

    def Draw(self, text):
        if self.__State == 0:
            self.__text = text
            Tree = self.Parse(text)
            for line in Tree:
                for sentence in line:
                    #print(type(sentence))
                    return sentence
            """
            for line in Tree:
                for sentence in line:
                    sentence.draw()"""
        else:
            return "Wrong Mode"

    def Tag(self, text):
        if self.__State == 1:
            self.__text = text
            #for line in list(self.__stf_parser.tag(self.__stf_parser.tokenize(text))):
            #    print(line)"""
            return list(self.__stf_parser.tag(self.__stf_parser.tokenize(text)))
        else:
            return "Wrong Mode"