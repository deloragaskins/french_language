#https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/


import spacy

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='french')

import spacy
from spacy import displacy
nlp = spacy.load("fr_core_news_sm")

#simple
#from spacy.lang.fr import French
# Create the nlp object
#nlp = French()

###python -m spacy download fr_core_news_sm


def return_token(sentence):
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner le texte de chaque token
    return [X.text for X in doc]

def return_POS(sentence):
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner les étiquettes de chaque token
    return [(X, X.pos_) for X in doc]

###############################################################


def return_stem(sentence):
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]


########################################################
# import spacy
# from spacy import displacy
# nlp = spacy.load("fr_core_news_sm")
# doc = nlp(sentence)
# displacy.render(doc, style="ent", jupyter=True)
