from configparser import SafeConfigParser
import os
import sys

def outpath_websource(websourcechoice):
    parser = SafeConfigParser()
    parser.read('./setup/user.ini')
    candidate='OS'
    print(parser.has_section(candidate))
    user_OS=parser.get('OS', 'user_OS')
    user_OS=user_OS[1:-1]
    print (user_OS)

    if websourcechoice=='journal_en_francais_facile' or 'AZ_lyrics':
        if user_OS=='Windows':
            spacer_char='\\'
        elif user_OS=='Ubuntu':
            spacer_char='/'
        else:
            print('invalid OS')
        outpath_loc=parser.get('file_locations', 'local_data_dir')
        outpath_loc=outpath_loc[-1:-1]
        outpath = outpath_loc+spacer_char+ websourcechoice +spacer_char
        if not os.path.exists(outpath):
            os.makedirs(outpath)
    else:
        print('invalid webresourcechoice')

    return outpath
