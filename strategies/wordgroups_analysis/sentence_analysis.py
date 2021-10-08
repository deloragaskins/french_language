import nltk
import strategies.inputs_file as InF
import spacy
import random

def recreate_sentence(sentence):

    tokens = nltk.word_tokenize(sentence)
    tokens_removable=tokens.copy()
    tokens_shuffle=tokens.copy()
    print(sentence)

    #random.shuffle(tokens_shuffle)
    #print(tokens_shuffle)
    #tokens_removable=tokens_shuffle.copy()

    verbs=InF.user_inputter('find verbs')

    #find article/noun accords
    article_noun_accords_list=[]
    helping_piece='phrases'
    info_message_str='Enter '+helping_piece +' one at a time and then press enter'
    print(info_message_str)
    info_message_str='When done type \'finished\''
    print(info_message_str)

    new_set=InF.user_inputter('find '+helping_piece)
    while new_set !='finished':

        new_set_tokens=nltk.word_tokenize(new_set)

        valid_check=0
        for token in new_set_tokens:
            if token in tokens_removable:
                valid_check+=1

        if valid_check == len(new_set_tokens):
            article_noun_accords_list.append(new_set)
            for tokens in new_set_tokens:
                tokens_removable.remove(tokens)
        else:
            print('please check for typos and try again')
        new_set=InF.user_inputter('find '+helping_piece)
        #print(new_set_tokens)
        #print(tokens_removable)
    random.shuffle(tokens_removable)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('verbs:'+ verbs)
    print('helping sets found:'+ str(article_noun_accords_list))
    print('leftovers:' +str(tokens_removable))

    sentence_attempt=str(InF.user_inputter('Type the sentence'))
    print(sentence)
    return

def parts_of_speech_finder(sentence):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(sentence)
    word_list=[]
    parts_list=[]
    for token in doc:
        # #     #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        # #     #            token.shape_, token.is_alpha, token.is_stop)
        word_list.append(token.text)
        parts_list.append(token.pos_)

    #print(word_list)
    #print(parts_list)
    return word_list,parts_list

def extract_verbs (sentence):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(sentence)
    word_list=[]
    for token in doc:
        # #     #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        # #     #            token.shape_, token.is_alpha, token.is_stop)
        if token.pos_ =='VERB':
            word_list.append(token.text)
    return word_list



    # nouns=InF.user_inputter('find subject')
    #
    # print('le COD répond à la question « Qui ? » ou « Quoi ?')
    # nouns=InF.user_inputter('find COD')
    # print('répond à la question : « À qui ? À quoi ? De qui ? De quoi ? »')
    # nouns=InF.user_inputter('find COD')
    #return
