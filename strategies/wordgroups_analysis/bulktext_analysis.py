import strategies.inputs_file as InF
import nltk

def function_doer_for_all_sentences(bulk_text,function_to_be_done):

    for counter3 in range(len(bulk_text)) :
        paragraph_number=counter3
        paragraph=bulk_text[paragraph_number]
        sentences_list=nltk.sent_tokenize(paragraph)
        total_sentences_in_paragraph=len(sentences_list)
        for counter4 in range(total_sentences_in_paragraph):
            sentence_number=counter4
            sentence=return_sentence(bulk_text,paragraph_number,sentence_number)
            outputs_FTBD=function_to_be_done(sentence)

def word_finder(bulk_text):

    info_message_str='input keyword'
    word_sought=str(InF.user_inputter(info_message_str))
    in_sentences=[]
    in_paragraph=[]
    in_paragraph_index=0
    for paragraph in bulk_text:
        sentences_list=nltk.sent_tokenize(paragraph)
        in_sentence_index=0
        for sentence in sentences_list:
            tokens = nltk.word_tokenize(sentence)
            if word_sought in tokens:
                #print(sentence)
                in_sentences.append(in_sentence_index)
                in_paragraph.append(in_paragraph_index)

            in_sentence_index+=1
        in_paragraph_index+=1
    return in_sentences,in_paragraph

def phrase_finder(bulk_text):
    info_message_str='input phrase'
    phrase_sought=str(InF.user_inputter(info_message_str))
    in_sentences=[]
    in_paragraph=[]
    in_paragraph_index=0
    for paragraph in bulk_text:
        sentences_list=nltk.sent_tokenize(paragraph)
        in_sentence_index=0
        for sentence in sentences_list:
            if phrase_sought in sentence:
                #print(sentence+'\n')
                in_sentences.append(in_sentence_index)
                in_paragraph.append(in_paragraph_index)
            in_sentence_index+=1
        in_paragraph_index+=1
    return in_sentences,in_paragraph

def return_sentence(bulk_text,paragraph_number,sentence_number):
    paragraph=bulk_text[paragraph_number]
    sentences_list=nltk.sent_tokenize(paragraph)
    total_sentences_in_paragraph=len(sentences_list)
    sentence=sentences_list[sentence_number]
    return sentence

def printbulk_paragraphs(bulk_text):
    print('begin print')
    print('type Q to end printing')
    print('type enter to continue printing')

    for paragraph in bulk_text:
        inp=InF.user_inputter(' ')
        if inp=='Q':
            break
        print (paragraph)
