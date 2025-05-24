'''
Module designed for document processing such as:
 - converting from internal VocabList object to json output
 - converting from json to internal VocabList object
'''

import json
from wordclass import Word, VocabList
import os





def json_to_list(filename: str = 'vocab.json'):

    '''converts json contents to a VocabList object'''


    with open(filename, 'r', encoding = 'utf-8') as f:
        json_contents = json.load(f)

    return VocabList([Word.from_dict(word_dict) for word_dict in json_contents ])





'''dependencies'''

#------------------------------------------------------------------------------------------

'''important module functions'''





def list_to_json(vocablist: VocabList, filename: str = 'vocab.json'):

    '''creates a json file populated with contents from current VocabList object'''


    #utf-8 is cross compatible

    with open(filename, 'w', encoding = 'utf-8') as j:


        def word_to_dict(word: Word):
            return {'word': word.name, 'examples': word.examples}


        #ensure_ascii off can allow accented or special unicode characters
        #indentation used so the .json file is human-readable

        json.dump([word_to_dict(entry) for entry in vocablist], j, ensure_ascii = False, indent = 2)







def read_from_json():

    '''reads from json to VocabList;  returns object if file exists, none if it does not'''


    selection = input('Which .json file do you want to draw from? ')


    #if user forgot the .json extension
    if not selection.endswith('.json'):
        selection += '.json'


    #only read from files that exist
    if os.path.exists(selection):

        #vocablist is the VocabList object we create from the json file
        vocablist = json_to_list(selection)
        print('List generated from', selection)
        return vocablist


    print("File does not exist")

