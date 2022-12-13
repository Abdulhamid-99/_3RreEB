import Server

hrkat = {"fatha":"ً","dmah":"ُ","ksrah":"ِ","fatha2":"ً","dmah2":"ٌ","ksrah2":"ٍ","shadah":"ّ","sokon":"ْ"}

def printer(s):
    for line in s:
        print(line)

text = u'ذهب خالد إلى الحديقة'

Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
#print(Tagger.Tag(text))
sentences = Tagger.Tag(text)
printer(sentences)

Parser = Server._3RreEB("http://139.59.210.136:9005",0)
Parser.Draw(text)
#print(Parser.Parse(text))

t = u'ولد'
if True:
    t = t+hrkat["dmah2"]
print(t)

