from document_processing import word_to_list, list_to_json
from wordclass import Word, VocabList
import os



def help():

    commands = ['\nCommands:', '(0) exit', '(1) reprint help' ,'(2) read from docx', '(3) search by word', 
                '(4) show current vocab list', '(5) create json from current vocab list']

    for line in commands:
        print(line)



def program():

    help()

    #only accepts numerical inputs
    #0 ends the program


    vocabulary = None


    while (command := int(input('\ncommand: '))) != 0:
        
    

        #show the help window again
        if command == 1:

            help()
        


        #read from docx file(s) to a VocabList object
        elif command == 2:

            files = []
            while (docxfile := input("Add .docx files to parse (blank to stop inputting): ")):

                #if user input is valid
                if os.path.exists(docxfile):
                    files.append(docxfile)

                #if user input is invalid
                else:
                    print('Such a file does not exist in the program folder')


            vocabulary = VocabList(word_to_list(files))        



        #search for specific word
        elif command == 3:

            which_word = input("\nWhich word are you looking for? ")

            print('\n'+vocabulary.search_for_word(which_word))




        #show the current vocablist and its length
        elif command == 4:
            print(vocabulary)




        #generate a JSON from the selected list
        elif command == 5:


            json_file_name = input("\nWhat do you want the .json to be called? ")

            list_to_json(vocabulary, json_file_name)





if __name__ == "__main__":
    program()