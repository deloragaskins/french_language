from configparser import SafeConfigParser
import os
import sys

def outpath_websource(websourcechoice):
    parser = SafeConfigParser()
    parser.read('./setup/user.ini')
  
    if websourcechoice=='journal_en_francais_facile' or 'AZ_lyrics':
        outpath_loc=parser.get('file_locations', 'local_data_dir')
        outpath = os.path.join(output_loc.split(os.sep) + websourcechoice) + os.sep
        
        if not os.path.exists(outpath):
            os.makedirs(outpath)
    else:
        print('invalid webresourcechoice')

    return outpath
