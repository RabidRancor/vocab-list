'''
Module designed for document processing such as:
 - converting from docx to internal VocabList object
 - converting from internal VocabList object to json output
 - converting from json to internal VocabList object
'''

import docx
import json
from wordclass import Word, VocabList
import os



def word_to_list(files: list):

    '''Extracts content from arbitrary amount of docx files and converts it to a list of dictionaries'''

    finaloutput = []

    #file = file name from a list of file names
    for file in files:


        #our file read object
        doc = docx.Document(file)


        current_word = ""
        current_examples = []



        #each paragraph in the document
        for paragraph in doc.paragraphs:
            
            #extract the paragraph as a string with newline/carriage return removed
            text = paragraph.text.strip()

            #empty paragraph is ignored
            if not text:
                continue



            #check the runs in this paragraph for any evidence of bolding
            #bold is a Boolean flag
            #if it detects any bolded runs, it outputs a True


            bold = any(run.bold for run in paragraph.runs)



            #if the paragraph is bold text
            if bold:


                #if the current line is a bold one
                #and there is a value already in current_word
                #then that means you're onto the next word and should upload
                #the previous word and examples to the list as Word objects

                #this is only triggered when you reach the second word and onwards

                if current_word:

                    word_to_add = Word(current_word)
                    for example in current_examples:
                        word_to_add.add_example(example)
                    
                    finaloutput.append(word_to_add)
                

                #currentword is set whenever a bold paragraph is detected
                #and current_examples is cleared
                current_word = text
                current_examples = []
                

                
            #if the current paragraph is not bold
            #then it is an example for current_word
            #and should be appended to the list

            else:
                current_examples.append(text)




        #when the above code reaches the last word, it will fill current_word and current_examples
        #but wont be able to trigger that nested if statement for current_word
        #so the for loop will end but current_word and current_examples retain their contents
        #since they're global variables

        if current_word:
            word_to_add = Word(current_word)
            for example in current_examples:
                word_to_add.add_example(example)
            
            finaloutput.append(word_to_add)


    return finaloutput







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







def read_from_docx():

    '''reads from docx to VocabList;  returns object if file(s) exist, none of it does not'''

    files = []

    while (docxfile := input("Add .docx files to parse (blank to stop inputting): ")):

        #if user forgot the .docx extension
        if not docxfile.endswith('.docx'):
            docxfile += '.docx'


        #if user input is valid
        if os.path.exists(docxfile):
            files.append(docxfile)
            print(docxfile, 'successfully inputted')


        #if user input is invalid
        else:
            print('File does not exist')


    #if the field is not empty
    if files:
        vocablist = VocabList(word_to_list(files)) 
        return vocablist 
