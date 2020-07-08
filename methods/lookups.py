def lookup_words(dictionary_choice):
    import webbrowser
    import strategies.inputs_file as InF
    import nltk
    #print(sentence)
    word_list_string=str(InF.user_inputter('list unknown words'))

    word_list = nltk.word_tokenize(word_list_string)

    print(word_list)

    #print('Dictionary choices are:Linguee')
    for word in word_list:
        if dictionary_choice=='Linguee':
            url='https://www.linguee.com/english-french/search?source=auto&query=+'+word
            webbrowser.open(url, new=0)
        elif dictionary_choice=='wordreference':
            url='https://www.wordreference.com/fren/'+word
            webbrowser.open(url, new=0)
        else:
            print('dictionary unknown')
