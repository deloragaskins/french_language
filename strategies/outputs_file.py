from configparser import SafeConfigParser
import os
import sys

def outpath_websource(websourcechoice):
    parser = SafeConfigParser()
    parser.read('../setup/user.ini')
    candidate='OS'
    print(parser.has_section(candidate))
    print (parser.get('OS', 'user_OS'))


    if websourcechoice=='journal_en_francais_facile' or 'AZ_lyrics':
        outpath_loc==parser.get('file_locations', 'local_data_dir')
        if user_OS=='Windows':
            outpath = outpath_loc+'\\'+ websourcechoice +'\\'
        if user_OS=='Ubuntu':
            outpath = outpath_loc+'/'+websourcechoice +'/'
        if not os.path.exists(outpath):
            os.makedirs(outpath)
    else:
        print('invalid webresourcechoice')

    return outpath
