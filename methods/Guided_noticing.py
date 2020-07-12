import numpy as np
import nltk
import strategies.inputs_file as InF
import strategies.wordgroups_analysis.bulktext_analysis as BTA
import strategies.wordgroups_analysis.sentence_analysis as SA


def print_sentences_containing_word(bulk_text):
    in_sentences,in_paragraph=BTA.word_finder(bulk_text)

    info_message_str='pick a sentence number (less than '+str(len(in_sentences))+' but no less than 0) to start with:'
    start_num=int(InF.user_inputter(info_message_str))

    continuer='y'
    info_message_str='Press the y key  to continue or n key to stop if the program is waiting \n'
    print(info_message_str)
    spacing_str='********************************************************************'
    print(spacing_str)
    print(spacing_str)
    print(spacing_str)
    print(spacing_str)


    for counter1 in np.arange(start_num,len(in_sentences)):
        while continuer=='y':
            sentences_list=nltk.sent_tokenize(bulk_text[in_paragraph[counter1]])
            print('\n')
            print(sentences_list[in_sentences[counter1]])
            info_message_str=' \n waiting \n'
            continuer=InF.user_inputter(info_message_str)
    return

def recreate_sentences_containing_word(bulk_text):
    in_sentences, in_paragraph=BTA.word_finder(bulk_text)

    info_message_str='pick a sentence number (less than '+str(len(in_sentences))+' but no less than 0) to start with:'
    start_num=int(InF.user_inputter(info_message_str))

    continuer='y'
    info_message_str='Press the y key  to continue (or any other key to stop) if the program is waiting \n'
    print(info_message_str)
    spacing_str='********************************************************************'
    print(spacing_str)
    print(spacing_str)
    print(spacing_str)
    print(spacing_str)

    for counter1 in np.arange(start_num,len(in_sentences)):

        if continuer=='y':
            sentence_number=in_sentences[counter1]
            sentences_list=nltk.sent_tokenize(bulk_text[in_paragraph[counter1]])
            sentence=sentences_list[sentence_number]
            SA.recreate_sentence(sentence)
            info_message_str=' \n waiting \n'
            continuer=InF.user_inputter(info_message_str)
    return
