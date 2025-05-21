from docproc import word_to_list, list_to_json, json_to_list
from wordclass import Word, VocabList
import os



def help():

    '''displays command menu'''

    commands = ['Commands:', '(0) Exit', '(1) Help', '(2) Read from json', 
                '(3) Read from docx', '(4) Write to json', '(5) Show vocab list', 
                '(6) Add word', '(7) Add example', '(8) Remove word', 
                '(9) Search by word'
                ]

    for line in commands:
        print(line)





def program():

    '''main frontend interface for accessing vocab lists'''



    help()



    vocabulary = None


    while (command := (input('\ncommand: '))) != '0':
        

        #if user doesnt input an integer, just do nothing
        if not command.isdigit():
            print('Invalid command')
            pass
        else:
            command = int(command)
            print()





        #show the help window again
        if command == 1:

            help()
        




        #read from json file to VocabList object
        elif command == 2:

            selection = input('Which .json file do you want to draw from? ')


            #if user forgot the .json extension
            if not selection.endswith('.json'):
                selection += '.json'


            #only read from files that exist
            if os.path.exists(selection):
                vocabulary = json_to_list(selection)
                print('List generated from', selection)

            else:
                print("File does not exist")





        #read from docx file(s) to a VocabList object
        elif command == 3:

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


            if files:
                vocabulary = VocabList(word_to_list(files))        





        #generate a json from the selected list
        elif command == 4:


            #if the vocab list is None/empty
            if not vocabulary:
                print('No vocab list')
                continue


            json_file_name = input("\nWhat do you want the .json to be called? ")


            #if the user didn't type .json file extension, append it
            if not json_file_name.endswith('.json'):
                json_file_name += '.json'


            #DO NOT ALLOW FILE OVERWRITES
            #input file is read only

            if os.path.exists(json_file_name):
                print('File overwrite not allowed')
                continue


            #if the file name is not-empty
            if json_file_name:
                list_to_json(vocabulary, json_file_name)
                print('List written to', json_file_name)
                break

            else:
                print('Empty file name')





        #show the current vocablist and its length
        elif command == 5:

            print(vocabulary)





        #add a word to the list
        elif command == 6:

            #if there is no vocab list to look in
            if not vocabulary:
                print('No vocab list')
                continue


            what_word = input("Word to add: ")
            

            print(vocabulary.add_word(what_word))





        #add example for a word
        elif command == 7:

            if not vocabulary:
                print('No vocab list')
                continue


            mainword = input("Example for what word? ")

            #if word is in list
            if vocabulary.search_for_word(mainword):

                example = input('Example: ')
                print(vocabulary.add_example(mainword, example))
            
            else:
                print('Word not in list')

            
            


        #delete word
        elif command == 8:

            if not vocabulary:
                print('No vocab list')
                continue


            word2delete = input('Word to delete: ')

            if vocabulary.search_for_word(word2delete):

                print(vocabulary.delete_word(word2delete))

            else:

                print('Word not in list')





        #search for specific word
        elif command == 9:

            if not vocabulary:
                print('No vocab list')
                continue


            which_word = input("Which word are you looking for? ")


            #if the word is in the list
            if (wordfound := vocabulary.search_for_word(which_word)):
                print(wordfound)

            else:
                print('Word not in list')








if __name__ == "__main__":
    program()