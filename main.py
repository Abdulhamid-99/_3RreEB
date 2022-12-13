import Server

text = u'ذهب خالد إلى الحديقة'

Parser = Server._3RreEB("http://139.59.210.136:9005",0)
print(Parser.Parse(text))

Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
print(Tagger.Tag(text))

