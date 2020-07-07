executor_name='sample_runner'
import nltk
import random
#nltk.download()

import methods.sentence_analysis as SA


sentence='Les États-Unis compte un nouveau candidat à la présidence.'
sentence='Cette journée de dimanche est marquée par un double scrutin'
#sentence='Avant cette annonce, la journée de dimanche a été l\'occasion pour le président  Emmanuel Macron et son nouveau Premier ministre Jean Castex de poursuivre les consultation, dans le but de constitué la nouvelle équipe gouvernementale'
#sentence='L\'artiste, milliardaire a fait cette annonce sur Twitter'

SA.recreate_sentence(sentence)
