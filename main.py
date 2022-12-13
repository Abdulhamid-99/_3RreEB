import Server

hrkat = {"fatha":"ً","dmah":"ُ","ksrah":"ِ","fatha2":"ً","dmah2":"ٌ","ksrah2":"ٍ","shadah":"ّ","sokon":"ْ"}

def printer(sentences):
    for sentence in sentences:
        print(sentence)

text = u'ذهب خالد إلى الحديقة'

Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
sentences = Tagger.Tag(text)
printer(sentences)

Parser = Server._3RreEB("http://139.59.210.136:9005",0)
Parser.Draw(text)

t = u'ولد'
if True:
    t = t+hrkat["dmah2"]
print(t)

