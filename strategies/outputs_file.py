exec(open('header.py').read())
import os


def outpath_websource(websourcechoice):

    if websourcechoice=='journal_en_francais_facile' or 'AZ_lyrics':
        outpath_loc=output_dir1
        if user_OS=='Windows':
            outpath = outpath_loc+'\\'+ websourcechoice +'\\'
        if user_OS=='Ubuntu':
            outpath = outpath_loc+'/'+websourcechoice +'/'
        if not os.path.exists(outpath):
            os.makedirs(outpath)
    else:
        print('invalid webresourcechoice')

    return outpath
