from nltk.corpus import words
import requests

import Server

hrkat = {"fatha":"ً","dmah":"ُ","ksrah":"ِ","fatha2":"ً","dmah2":"ٌ","ksrah2":"ٍ","shadah":"ّ","sokon":"ْ"}

def printer(sentences):
    for word in sentences:
        print(word)
        if is_verb(word):
            word = add_diacritics_to_verb(word)
        # If the word is a noun, add diacritics to the second and third radicals
        elif is_noun(word):
                word = add_diacritics_to_noun(word)
        # If the word is a pronoun, add diacritics to the second radical
        elif is_pronoun(word):
            word = add_diacritics_to_pronoun(word)
        # Otherwise, add diacritics to the first radical
        else:
            word = add_diacritics_to_first_radical(word)
        # Replace the original word in the list with the diacriticized version
        #sentences[i] = word

    # Join the list of words back into a sentence and return it
    #return " ".join(sentences)

def is_verb(word):
    # Determine if the word is a verb
    # Return True if it is, False otherwise
    pass

def is_noun(word):
    # Determine if the word is a noun
    # Return True if it is, False otherwise
    pass

def is_pronoun(word):
    # Determine if the word is a pronoun
    # Return True if it is, False otherwise
            pass

def add_diacritics_to_verb(word):
    # Add diacritics to the third radical of the verb
    pass

def add_diacritics_to_noun(word):
    # Add diacritics to the second and third radicals of the noun
    pass

def add_diacritics_to_pronoun(word):
    # Add diacritics to the second radical of the pronoun
            pass

def add_diacritics_to_first_radical(word):
    # Add diacritics to the first radical of the word
    pass



text = u'ادرسْ كي تنجحَِ'

Tagger = Server._3RreEB("http://139.59.210.136:9005",1)
sentences = Tagger.Tag(text)
printer(sentences)

Parser = Server._3RreEB("http://139.59.210.136:9005",0)
Parser.Draw(text)

t = u'ولد'
if True:
    t = t+hrkat["dmah2"]
print(t)

