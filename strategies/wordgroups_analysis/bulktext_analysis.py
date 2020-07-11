def return_sentence(bulk_text,paragraph_number,sentence_number):
    import nltk
    paragraph=bulk_text[paragraph_number]
    sentences_list=nltk.sent_tokenize(paragraph)
    total_sentences_in_paragraph=len(sentences_list)
    sentence=sentences_list[sentence_number]
    return sentence

