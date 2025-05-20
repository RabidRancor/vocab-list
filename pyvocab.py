
def help():

    '''displays command menu'''

    commands = ['Commands:', '(0) exit', '(1) help' ,'(2) read from docx', 
                '(3) read from json', '(4) search by word', '(5) show current vocab list', 
                '(6) add a word to the list', '(7) create json from current vocab list']

    for line in commands:
        print(line)





def program():

    '''main frontend interface for accessing vocab lists'''


    from docproc import word_to_list, list_to_json, json_to_list
    from wordclass import Word, VocabList
    import os



    help()



    vocabulary = None


    while (command := (input('\ncommand: '))) != '0':
        

        #if user doesnt input an integer, just do nothing
        if not command.isdigit():
            print('invalid command')
            pass
        else:
            command = int(command)
            print()



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
                    print(docxfile, 'successfully inputted')


                #if user input is invalid
                else:
                    print('Such a file does not exist in the program folder')


            if files:
                vocabulary = VocabList(word_to_list(files))        




        #read from json file to VocabList object
        elif command == 3:

            selection = input('Which .json file do you want to draw from? ')

            #only read from files that exist
            if os.path.exists(selection):
                vocabulary = json_to_list(selection)
                print('List generated from', selection)

            else:
                print("Such a file does not exist in the current folder")





        #search for specific word
        elif command == 4:

            #if there is a vocab list to look in
            if vocabulary:
                which_word = input("\nWhich word are you looking for? ")
                print('\n'+vocabulary.search_for_word(which_word))

            
            else:
                print('No vocab list to parse')





        #show the current vocablist and its length
        elif command == 5:

            print(vocabulary)




        #add a word to the list
        elif command == 6:

            if not vocabulary:
                print('No vocab list to append')
                continue


            what_word = input("Word to add: ")
            
            if what_word.strip():
                worked = vocabulary.add_word(what_word)
            else:
                print('empty field')
                continue

            #check if word was successfully added (case insensitive)
            if worked:
                print(f'Successfully added {what_word} to list')
            else:
                print(f'Word already in list')




        #generate a json from the selected list
        elif command == 7:


            #if the vocab list is None/empty
            if not vocabulary:
                print('No vocab list to upload')
                continue

            else:
                json_file_name = input("\nWhat do you want the .json to be called? ")


            #if the file name is not-empty
            if json_file_name:
                list_to_json(vocabulary, json_file_name+'.json')
                print('List written to', json_file_name)
                break

            else:
                print('Empty file name')





if __name__ == "__main__":
    program()