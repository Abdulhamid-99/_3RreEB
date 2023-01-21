import Server
from nltk.tree import Tree
import json
from collections import deque


hrkat = {"fatha":"\u0618", "dmah":"\u0619","ksrah":"\u061A","fathatan":"\u064B","dmatan":"\u064C","ksratan":"\u064D","shaddah":"\u0651","sukun":"\u0652"}

#def printer(sentences):
#    for sentence in sentences:
#        print(sentence)

text = u'إذهب إلى الجامعة'

#Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
#Parsed_Text = Tagger.Tag(text)
#print(Parsed_Text)




Parser = Server._3RreEB("http://139.59.210.136:9005",0)

Parsed_Text = Parser.Draw(text)
#print(Parsed_Text)
#print(Tree.pos(Parsed_Text))

def nltk_tree_to_python(tree: Tree):
    def convert(node):
        if isinstance(node, Tree):
            return {node.label(): [convert(child) for child in node]}
        else:
            return node
    return convert(tree)

#{'S': [{'VP': [{'VBD': ['اكل']}, {'NP': [{'NNP': ['محمد']}]}, {'NP': [{'DTNN': ['التفاحة']}]}]}]}
def extract_values(d):
    result = []
    stack = [d]
    while stack:
        current = stack.pop()
        print(current)
        if isinstance(current, dict):
            for key, value in current.items():
                stack.append(value)
        elif isinstance(current, list):
            for item in current:
                stack.append(item)
        else:
            result.append(current)
    return result


TreeType = nltk_tree_to_python(Parsed_Text)
result = []
for key, val in TreeType.items():
    if key =="S":
        print("تم التعرف على الجملة يا بابا")
        for k, v in val[0].items():
            if k == "VP":
                print(k)
                print("جملة فعلية")
                counter = 0
                for word in v:
                    if isinstance(word, dict):
                        for k1, v1 in word.items():
                            print(k1)
                            if k1 == "VBD":
                                print("فعل ماضي")
                                for v2 in v1:
                                    if isinstance(v2, str):
                                        result.append(v2+hrkat["fatha"])
                                    elif isinstance(v2, dict):
                                        for k3, v3 in v2.items():
                                            result.append(v3[0])
                                counter+=1
                                break
                            elif k1 == "VBP":
                                print("فعل مضارع")
                                for v2 in v1:
                                    if isinstance(v2, str):
                                        result.append(v2+hrkat["dmah"])
                                    elif isinstance(v2, dict):
                                        for k3, v3 in v2.items():
                                            result.append(v3[0])
                                counter+=1
                                break
                            elif k1 == "NP":
                                print("فاعل")
                                for v2 in v1:
                                    if counter == 1:
                                        if isinstance(v2, str):
                                            if v2[:2] == "ال":
                                                result.append(v2+hrkat["dmah"])

                                            else:
                                                result.append(v2+hrkat["dmatan"])

                                        elif isinstance(v2, dict):
                                            for k3, v3 in v2.items():
                                                if v3[0][:2] == "ال":
                                                    result.append(v3[0] + hrkat["dmah"])

                                                else:
                                                    result.append(v3[0]+hrkat["dmatan"])
                                    elif counter == 2:
                                        if isinstance(v2, str):
                                            result.append(v2 + hrkat["fatha"])
                                        elif isinstance(v2, dict):
                                            for k3, v3 in v2.items():
                                                result.append(v3[0] + hrkat["fatha"])
                                    counter += 1
                                break
                    """
                            elif (((k1 == "NP") and (counter == 2)) or ((k1 == "DTJJ") and (counter == 2))):
                                print("مفعول به")
                                for v2 in v1:
                                    if isinstance(v2, str):
                                        result.append(v2+hrkat["fatha"])
                                    elif isinstance(v2, dict):
                                        for k3, v3 in v2.items():
                                            result.append(v3[0]+hrkat["fatha"])
                                break
                            #---------------------------------
                            for v2 in v1:
                                if isinstance(v2, str):
                                    result.append(v2)
                                elif isinstance(v2, dict):
                                    for k3,v3 in v2.items():
                                        result.append(v3[0])
                    counter += 1
                    break
                    
                    elif isinstance(word, list):
                        for item in word:
                            result.append(item[0])
                    """

            if k == "NP":
                print("جملة أسميه")
                print(type(v))
                if isinstance(v, str):
                    if v[:2] == "ال":
                        result.append(v + hrkat["dmah"])

                    else:
                        result.append(v + hrkat["dmatan"])

                elif isinstance(v, list):
                    for v3 in v:
                        if v3[:2] == "ال":
                            result.append(v3 + hrkat["dmah"])

                        else:
                            result.append(v3+ hrkat["dmatan"])
    else:
        print("لم يتم التعرف على الجملة اتسوق امها يا غلام")


print(" ".join(result))

print(TreeType)
#print(extract_values(TreeType))
"""
for key, value in TreeType.items():
    print(key)
    for key1 in value:
        print(key1)
        if key1 == "VP":
            print("جملة فعلية")
        if key1 == "NP":
            print("جملة أسميه")
"""

"""
def nltk_tree_to_python(tree: Tree):
    return json.loads(tree.pformat())

#tree = Tree.fromstring("(S (NP (DT the) (JJ big) (NN dog)) (VP (VBD barked)))")
tree = Parsed_Text
python_tree = nltk_tree_to_python(tree)
print(python_tree)"""
"""

t = u'ولد'
if True:
    t = t+hrkat["dmah2"]
print(t)
"""


