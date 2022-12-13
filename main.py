import Server

text = u'ذهب خالد إلى الحديقة'

Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
print(Tagger.Tag(text))

Parser = Server._3RreEB("http://139.59.210.136:9005",0)
Parser.Draw(Parser.Parse(text))
print(Parser.Parse(text))

