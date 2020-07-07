import nltk
import strategies.inputs_file as InF

def recreate_sentence(sentence):
    import random
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
    all_found=str(InF.user_inputter('Are all of the articles/nouns listed:yes or no'))
    while all_found=='no':
        new_pair=InF.user_inputter('find article noun/accords')
        article_noun_accords_list.append(new_pair)
        new_pair_tokens=nltk.word_tokenize(new_pair)
        print(new_pair_tokens)
        tokens_removable.remove(new_pair_tokens[0])
        tokens_removable.remove(new_pair_tokens[1])
        random.shuffle(tokens_removable)
        print(tokens_removable)
        all_found=str(InF.user_inputter('Are all of the articles/nouns listed:yes or no'))

    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('verbs:'+ verbs)
    print('pairs found:'+ str(article_noun_accords_list))
    print('leftovers:' +str(tokens_removable))

    sentence_attempt=str(InF.user_inputter('Type the sentence'))
    print(sentence)
    return

def parts_of_speech_finder(sentence):
    # nouns=InF.user_inputter('find subject')
    #
    # print('le COD répond à la question « Qui ? » ou « Quoi ?')
    # nouns=InF.user_inputter('find COD')
    # print('répond à la question : « À qui ? À quoi ? De qui ? De quoi ? »')
    # nouns=InF.user_inputter('find COD')
    return
