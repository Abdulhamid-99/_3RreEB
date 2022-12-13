import Server
text = u'ذهب خالد إلى الحديقة'

Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
#print(Tagger.Tag(text))
Tagger.Tag(text)

Parser = Server._3RreEB("http://139.59.210.136:9005",0)
Parser.Draw(text)
#print(Parser.Parse(text))

hrkat = {"fatha":"ً","dmah":"ُ","ksrah":"ِ","fatha2":"ً","dmah2":"ٌ","ksrah2":"ٍ","shadah":"ّ","sokon":"ْ"}
t = u'ولد'
if True:
    t = t+hrkat["dmah2"]
print(t)