def word_finder(bulk_text):
    import strategies.inputs_file as InF
    import nltk
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
def return_sentence(bulk_text,paragraph_number,sentence_number):
    import nltk
    paragraph=bulk_text[paragraph_number]
    sentences_list=nltk.sent_tokenize(paragraph)
    total_sentences_in_paragraph=len(sentences_list)
    sentence=sentences_list[sentence_number]
    return sentence

