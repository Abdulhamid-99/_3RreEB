import Server
from nltk.tree import Tree
import json
from collections import deque


hrkat = {"fatha":"\u0618", "dmah":"\u0619","ksrah":"\u061A","fathatan":"\u064B","dmatan":"\u064C","ksratan":"\u064D","shaddah":"\u0651","sukun":"\u0652"}

#def printer(sentences):
#    for sentence in sentences:
#        print(sentence)
print("مرحباً بكم في عرّيب لتشكيل الكلمات بناءً على الإعراب")
print("-------------------------------------------------")
def parse(t):
    text = t
    reso = list()
    reso.append("----------------")
    #if text == "0":
        #break
    #Tagger = Server._3RreEB("http://139.59.210.136:9005",1)3RreEB3RreEB
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
    """
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
    """

    TreeType = nltk_tree_to_python(Parsed_Text)
    result = []
    for key, val in TreeType.items():
        if key == "S" or key == "NP":
            counter = 0
            jr = False
            print("تم التعرف على الجملة")
            reso.append("تم التعرف على الجملة")
            for index, value in enumerate(val):
                for k, v in value.items():
                    #print(len(v))
                    if k == "VP":
                        print(k)
                        print("جملة فعلية")
                        #reso.append(k)
                        reso.append("جملة فعلية")
                        for word in v:
                            if isinstance(word, dict):
                                for k1, v1 in word.items():
                                    #print(k1)
                                    if k1 == "VBD":
                                        print("فعل ماضي: ",end="")
                                        reso.append("فعل ماضي: ")
                                        if len(v) < 3:
                                            for v2 in v1:
                                                if isinstance(v2, str):
                                                    result.append(v2+hrkat["dmah"])
                                                    print(v2)
                                                    reso[-1] = reso[-1]+v2
                                                elif isinstance(v2, dict):
                                                    for k3, v3 in v2.items():
                                                        result.append(v3[0]+hrkat["dmah"])
                                                        print(v3[0])
                                                        reso[-1] = reso[-1]+v3[0]
                                            counter+=1
                                        else:
                                            for v2 in v1:
                                                if isinstance(v2, str):
                                                    result.append(v2+hrkat["fatha"])
                                                    print(v2)
                                                    reso[-1] = reso[-1]+v2
                                                elif isinstance(v2, dict):
                                                    for k3, v3 in v2.items():
                                                        result.append(v3[0]+hrkat["fatha"])
                                                        print(v3[0])
                                                        reso[-1] = reso[-1]+v3[0]
                                            counter+=1
                                        break
                                    elif k1 == "VBP":
                                        print("فعل مضارع: ",end="")
                                        reso.append("فعل مضارع: ")
                                        for v2 in v1:
                                            if isinstance(v2, str):
                                                result.append(v2+hrkat["dmah"])
                                                reso[-1] = reso[-1]+v2
                                            elif isinstance(v2, dict):
                                                for k3, v3 in v2.items():
                                                    result.append(v3[0])
                                                    reso[-1] = reso[-1]+v3[0]
                                        counter += 1
                                        break
                                    elif k1 == "NP":
                                        if len(v) < 3:
                                            print("فاعل: ", end="")
                                            reso.append("فاعل: ")
                                            reso[-1] = reso[-1]+"ضمير متصل"
                                            result[-1] = result[-1][:-1]
                                            print("مفعول به: ", end="")
                                            reso.append("مفعول به: ")
                                            if isinstance(v1, str):
                                                if v1[:2] == "ال":
                                                    result.append(v1 + hrkat["fatha"])
                                                    print(v1)
                                                    reso[-1] = reso[-1]+v1

                                                else:
                                                    result.append(v1 + hrkat["fathatan"])
                                                    print(v1)
                                                    reso[-1] = reso[-1]+v1
                                                # result.append(v2 + hrkat["fatha"])
                                                print(v1)
                                                reso[-1] = reso[-1]+v1
                                            elif isinstance(v1, dict):
                                                for k3, v3 in v1.items():
                                                    if k3 == "NN":
                                                        print("somthing wrong")
                                                        reso.append("خطأ في تركيب الجملة")
                                                        exit()
                                                    elif v3[0][:2] == "ال":
                                                        result.append(v3[0] + hrkat["fatha"])
                                                        print(v3)
                                                        reso[-1] = reso[-1]+v3

                                                    else:
                                                        result.append(v3[0] + hrkat["fathatan"])
                                                    # result.append(v3[0] + hrkat["fatha"])
                                                    print(v3[0])
                                                    reso[-1] = reso[-1]+v3[0]
                                            elif isinstance(v1, list):
                                                for k4, v4 in enumerate(v1):
                                                    for k5, v5 in v4.items():
                                                        if k5 == "NN":
                                                            print("خطأ في الجملة سيتم الخروج من عرّيب")
                                                            reso = list()
                                                            reso.append("خطأ في الجملة سيتم الخروج من عرّيب")
                                                            return reso
                                                        if isinstance(v5, list):
                                                            for k6, v6 in enumerate(v5):
                                                                if isinstance(v6, dict):
                                                                    for k7, v7 in v6.items():
                                                                        if v7[0][:2] == "ال":
                                                                            result.append(v7[0] + hrkat["fatha"])
                                                                            print(v)
                                                                            reso[-1] = reso[-1]+v

                                                                        else:
                                                                            result.append(v7[0] + hrkat["fathatan"])
                                                                        # result.append(v3[0] + hrkat["fatha"])
                                                                        print(v7[0])
                                                                        reso[-1] = reso[-1]+v7[0]
                                                                if v6[:2] == "ال":
                                                                    result.append(v6 + hrkat["fatha"])
                                                                    print(v6)
                                                                    reso[-1] = reso[-1]+v6

                                                                else:
                                                                    result.append(v6 + hrkat["fathatan"])
                                                                    print(v6)
                                                                    reso[-1] = reso[-1]+v6
                                                                # result.append(v3[0] + hrkat["fatha"])

                                                        else:
                                                            if v5[0][:2] == "ال":
                                                                result.append(v5[0] + hrkat["fatha"])
                                                                # print(v)

                                                            else:
                                                                result.append(v5[0] + hrkat["fathatan"])
                                                            #result.append(v5[0] + hrkat["fatha"])
                                                            print(v5[0])
                                                            reso[-1] = reso[-1]+v5[0]
                                            break
                                        else:
                                            for v2 in v1:
                                                if counter == 1:
                                                    print("فاعل: ",end="")
                                                    reso.append("فاعل: ")
                                                    if isinstance(v2, str):
                                                        if v2[:2] == "ال":
                                                            result.append(v2+hrkat["dmah"])
                                                            print(v2)
                                                            reso[-1] = reso[-1]+v2

                                                        else:
                                                            result.append(v2+hrkat["dmatan"])
                                                            print(v2)
                                                            reso[-1] = reso[-1]+v2

                                                    elif isinstance(v2, dict):
                                                        for k3, v3 in v2.items():
                                                            if k3 == "PRP":
                                                                if v3[0][:2] == "ال":
                                                                    result[-1] = result[-1][:-1]
                                                                    result.append(v3[0])
                                                                    print(v3[0])
                                                                    reso[-1] = reso[-1]+v3[0]

                                                                else:
                                                                    result[-1] = result[-1][:-1]
                                                                    result.append(v3[0])
                                                                    print(v3[0])
                                                                    reso[-1] = reso[-1]+v3[0]
                                                            else:
                                                                if v3[0][:2] == "ال":
                                                                    result.append(v3[0] + hrkat["dmah"])
                                                                    print(v3[0])
                                                                    reso[-1] = reso[-1]+v3[0]

                                                                else:
                                                                    result.append(v3[0]+hrkat["dmatan"])
                                                                    print(v3[0])
                                                                    reso[-1] = reso[-1]+v3[0]

                                                elif counter == 2:
                                                    print("مفعول به: ",end="")
                                                    reso.append("مفعول به: ")
                                                    if isinstance(v2, str):
                                                        if v2[:2] == "ال":
                                                            result.append(v2 + hrkat["fatha"])
                                                            print(v2)
                                                            reso[-1] = reso[-1]+v2

                                                        else:
                                                            result.append(v2 + hrkat["fathatan"])
                                                            print(v2)
                                                            reso[-1] = reso[-1]+v2
                                                        #result.append(v2 + hrkat["fatha"])
                                                        #print(v2)
                                                    elif isinstance(v2, dict):
                                                        for k3, v3 in v2.items():
                                                            if isinstance(v3, str):
                                                                if v3[:2] == "ال":
                                                                    result.append(v3 + hrkat["fatha"])
                                                                    print(v3)
                                                                    reso[-1] = reso[-1]+v3

                                                                else:
                                                                    result.append(v3 + hrkat["fathatan"])
                                                                    print(v3)
                                                                    reso[-1] = reso[-1]+v3
                                                                # result.append(v3[0] + hrkat["fatha"])

                                                            elif isinstance(v3, dict):
                                                                for k4, v4 in v3.items():
                                                                    if v4[0][:2] == "ال":
                                                                        result.append(v4[0] + hrkat["fatha"])
                                                                        print(v4[0])
                                                                        reso[-1] = reso[-1]+v4[0]

                                                                    else:
                                                                        result.append(v4[0] + hrkat["fathatan"])
                                                                        print(v4[0])
                                                                        reso[-1] = reso[-1]+v4[0]
                                                                    # result.append(v3[0] + hrkat["fatha"])

                                                            elif isinstance(v3, list):
                                                                for k4, v4 in enumerate(v3):
                                                                    if v4[:2] == "ال":
                                                                        result.append(v4 + hrkat["fatha"])
                                                                        print(v4)
                                                                        reso[-1] = reso[-1]+v4

                                                                    else:
                                                                        result.append(v4 + hrkat["fathatan"])
                                                                        print(v4)
                                                                        reso[-1] = reso[-1]+v4
                                                                    # result.append(v3[0] + hrkat["fatha"])

                                                counter += 1
                                        break

                                    elif k1 == "PP" :
                                        if len(v) < 3:
                                            print("فاعل: ", end="")
                                            reso.append("فاعل: ")
                                            print("ضمير متصل")
                                            reso[-1] = reso[-1]+"ضمير متصل"
                                            result[-1] = result[-1][:-1]
                                            jr = True
                                            print("حرف جر: ", end="")
                                            reso.append("حرف جر: ")
                                            for i2, v2 in enumerate(v1):
                                                if counter == 1:
                                                    if isinstance(v2, str):
                                                        result.append(v2)
                                                        print(v2)
                                                        reso[-1] = reso[-1]+v2
                                                    elif isinstance(v2, dict):
                                                        for k3, v3 in v2.items():
                                                            result.append(v3[0])
                                                            print(v3[0])
                                                            reso[-1] = reso[-1]+v3[0]
                                                    counter += 1
                                                elif counter == 2:
                                                    print("اسم مجرور: ", end="")
                                                    reso.append("اسم مجرور: ")
                                                    for k3, v3 in v2.items():
                                                        if isinstance(v3, str):
                                                            result.append(v3 + hrkat["ksrah"])
                                                            print(v3)
                                                            reso[-1] = reso[-1]+v3
                                                        elif isinstance(v3, dict):
                                                            for k4, v4 in v3.items():
                                                                result.append(v4[0] + hrkat["ksrah"])
                                                                print(v4[0])
                                                                reso[-1] = reso[-1]+v4[0]
                                                        elif isinstance(v3, list):
                                                            for k4, v4 in enumerate(v3):
                                                                for k5, v5 in v4.items():
                                                                    result.append(v5[0] + hrkat["ksrah"])
                                                                    print(v5[0])
                                                                    reso[-1] = reso[-1]+v5[0]

                                            break
                                        else:
                                            jr = True
                                            print("حرف جر: ",end="")
                                            reso.append("حرف جر: ",end="")
                                            for i2, v2 in enumerate(v1):
                                                if counter == 2:
                                                    if isinstance(v2, str):
                                                        result.append(v2)
                                                        print(v2)
                                                        reso[-1] = reso[-1]+v2
                                                    elif isinstance(v2, dict):
                                                        for k3, v3 in v2.items():
                                                            result.append(v3[0])
                                                            print(v3[0])
                                                            reso[-1] = reso[-1]+v3[0]
                                                    counter += 1
                                                elif counter == 3:
                                                    print("اسم مجرور: ", end="")
                                                    reso.append("اسم مجرور: ")
                                                    for k3, v3 in v2.items():
                                                        if isinstance(v3, str):
                                                            result.append(v3 + hrkat["ksrah"])
                                                            print(v3)
                                                            reso[-1] = reso[-1]+v3
                                                        elif isinstance(v3, dict):
                                                            for k4, v4 in v3.items():
                                                                result.append(v4[0] + hrkat["ksrah"])
                                                                print(v4[0])
                                                                reso[-1] = reso[-1]+v4[0]
                                                        elif isinstance(v3, list):
                                                            for k4, v4 in enumerate(v3):
                                                                for k5, v5 in v4.items():
                                                                    result.append(v5[0] + hrkat["ksrah"])
                                                                    print(v5[0])
                                                                    reso[-1] = reso[-1]+v5[0]

                                            break
                                """ 
                                    elif counter == 2:
                                        print("مفعول به: ",end="")
                                        for v2 in v1:
                                            if isinstance(v2, str):
                                                if v2[:2] == "ال":
                                                    result.append(v2 + hrkat["fatha"])
                                                    # print(v)

                                                else:
                                                    result.append(v2 + hrkat["fathatan"])
                                                    # print(v2)
                                                # result.append(v2 + hrkat["fatha"])
                                                print(v2)
                                            elif isinstance(v2, dict):
                                                for k3, v3 in v2.items():
                                                    if v3[0][:2] == "ال":
                                                        result.append(v3[0] + hrkat["fatha"])
                                                        # print(v)

                                                    else:
                                                        result.append(v3[0] + hrkat["fathatan"])
                                                    # result.append(v3[0] + hrkat["fatha"])
                                                    print(v3[0])
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
                    print(len(v))
                    if (k == "NP" or k == "ADJP"):
                        if len(v) < 3:
                            if counter == 0:
                                print("جملة اسميه")
                                reso.append("جملة اسميه")
                                print("مبتدأ: ",end="")
                                reso.append("مبتدأ: ")
                            else:
                                print("خبر: ",end="")
                                reso.append("خبر: ")
                            #print(type(v))
                            if isinstance(v, str):
                                if v[:2] == "ال":
                                    result.append(v + hrkat["dmah"])
                                    print(v)
                                    reso[-1] = reso[-1]+v

                                else:
                                    result.append(v + hrkat["dmatan"])
                                    print(v)
                                    reso[-1] = reso[-1]+v

                            elif isinstance(v, list):
                                for v3 in v:
                                    for k4, v4 in v3.items():
                                        if v4[0][:2] == "ال":
                                            result.append(v4[0] + hrkat["dmah"])
                                            print(v4[0])
                                            reso[-1] = reso[-1]+v4[0]

                                        else:
                                            result.append(v4[0]+ hrkat["dmatan"])
                                            print(v4[0])
                                            reso[-1] = reso[-1]+v4[0]
                            counter+=1
                        else:
                            reso = list()
                            reso.append("الجمل الاسمية المشمولة هي التي تتكون من مبتدأ وخبر فقط")
                            return reso

        else:
            print("لم يتم التعرف على الجملة")
            reso.append("لم يتم التعرف على الجملة")


    print(" ".join(result))

    print(TreeType)
    reso.append("الجملة المشكّلة: ")
    reso[-1] = reso[-1]+str(" ".join(result))
    #reso.append(str(TreeType))
    return reso



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


