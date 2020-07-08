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


def journal_en_francais_facile_puller(URL):
    import requests
    from bs4 import BeautifulSoup
    import urllib.request
    import strategies.outputs_file as OutF
    import nltk

    with urllib.request.urlopen(URL) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')


    all_divs=soup.find_all("div")
    for counter1 in range(len(all_divs)):
        #print(counter1)
        div_text_counter=all_divs[counter1].get_text()
        if div_text_counter=='Transcription':
            text_block=all_divs[counter1+1].get_text()

    websourcechoice='journal_en_francais_facile'
    outpath=OutF.outpath_websource(websourcechoice)
    identifier=soup.title.string

    identifier=identifier.replace("/", "")
    identifier=identifier.replace("Journal en français facile", "")
    identifier=identifier.replace("|", "")

    identifier=identifier.replace("20h00 GMT", "")
    identifier=identifier.replace("RFI SAVOIRS", "")
    print(identifier)
    identifier=identifier.replace(" ", "")


    filename=outpath+identifier+'.txt'

    sentences_list=nltk.sent_tokenize(text_block)
    with open(filename, 'w+') as f:
        # for sentence in sentences_list:
        #     f.write(sentence)
        #     f.write('\n')

         f.write(text_block)
    return filename
