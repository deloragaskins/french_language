executor_name='sample_runner'
import nltk
import random
#nltk.download()

import methods.sentence_analysis as SA
import methods.web_tools as web_tools

import strategies.inputs_file as InF

#######################################################################
URL='https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-fran%C3%A7aise/journal-en-francais-facile-03072020-20h00-gmt'
#database builders
filename=web_tools.journal_en_francais_facile_puller(URL)
######################################################################

list_of_sentences=InF.read_resource(filename)
sentence=list_of_sentences[0]
########################################################################
 #sentence_based functions###

#SA.recreate_sentence(sentence)



#web_tools.lookup_words()
#######################################################################
multiplier=int(InF.user_inputter('type multipler'))
baselist=[1,2,3,4,5,6,7,8,9,10]

print('**********************')
print('**********************')
print('**********************')
list_of_sentences=InF.read_resource(filename)
which_sentences=[element * multiplier for element in baselist]
for counter1 in which_sentences:
    sentence=list_of_sentences[counter1]
    sentence=sentence.replace("\n", "")
    print(sentence)
print(counter1)

print('**********************')
print('**********************')
print('**********************')
#SA.recreate_sentence(sentence)
web_tools.lookup_words()
