'''Contains frontend program for creating or editing a list or uploading to json'''



from docproc import list_to_json, read_from_docx, read_from_json
from wordclass import Word, VocabList
import os
from math import ceil
import keyboard
from time import sleep



def help():

    '''displays command menu'''

    commands = ['Commands:', '(0) Exit', '(1) Help', '(2) Read from json', 
                '(3) Read from docx', '(4) Write to json', '(5) Show vocab list', 
                '(6) Add word', '(7) Add example', '(8) Remove word', 
                '(9) Search by word', '(10) Empty list'
                ]

    for line in commands:
        print(line)






def program():

    '''Main frontend interface for editing VocabList objects'''



    help()



    vocabulary = None


    while (command := (input('\ncommand: '))) != '0':
        


        #if user doesnt input an integer, just do nothing
        if not command.isdigit():
            print('Invalid command')
            continue
        else:
            command = int(command)
            print()





        #show the help window again
        if command == 1:

            help()
        



        #read from json file to VocabList object
        elif command == 2:

            #ensure misinput or empty input doesnt clear list
            if (new_vocabulary_maybe := read_from_json()):

                vocabulary = new_vocabulary_maybe



        #read from docx file(s) to a VocabList object
        elif command == 3:

            #ensure misinput or empty input doesnt clear list
            if (new_vocabulary_maybe := read_from_docx()):

                vocabulary = new_vocabulary_maybe      



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

            else:
                print('Empty file name')





        #show the current vocablist and its length
        elif command == 5:


            if not vocabulary:
                print('No vocab list')
                continue


            #increment defines the window size
            #displaylist is the vocablist that gets generate on the fly
            #only increment elements of it are displayed
            #last page will have less elements if the listsize isnt divisible by the increment

            i = 0
            
            print(f'{len(vocabulary)} words in list')

            if (windowsize := input('How many words to display at a time? ')).isdigit() and int(windowsize) <= len(vocabulary):
                increment = int(windowsize)
                print()
            else:
                print('Invalid length')
                continue


            #apparently the keyboard module needs time to clear the buffer
            #so the enter press after inputting the number of words to display at a time
            #isn't registered by the scrolling logic

            while keyboard.is_pressed('enter'):
                sleep(0.05)


            maxindex = len(vocabulary) - 1
            displaylist = vocabulary



            pagecount = ceil(len(vocabulary)/increment)



            while True:


                pagenumber = (i//increment) + 1



                #the index you stop printing for is either the one at the end of your window 
                #or the end of the list if you dont have a full window to print
                
                end_index = min(i + increment, len(vocabulary))


                print('=' * 90)
                print(f'\n{VocabList(displaylist[i:end_index])}\n')
                print(f'\nPage {pagenumber} of {pagecount}')
                print(f'Words {i+1} to {end_index}\n')
                print('Scroll with arrow keys or WS, press ENTER to exit (ignore the buggy output)\n')

                keyboard.clear_all_hotkeys()



                #technically '' is a substring of any string, so we must strip it out to ignore empty cases
                keyboardpress = keyboard.read_key().strip()



                #due to an odd quirk with how python interacts with stdin buffer and the terminal input
                #i need to flush the newline created by the enter press
                #so we dont get a blank input to the command prompt that auto triggers
                #i cant remove the quirky buffer output tho

                if keyboardpress == 'enter':
                    input()
                    break




                if keyboardpress in ('w', 'up') and i >= increment:
                    i -= increment


                #stop scrolling if we cant increment the display window
                elif keyboardpress in ('s', 'down') and i + increment < len(vocabulary):
                    i += increment


                #we need to debounce the keyboard input
                #it is registering double presses because it updates too fast
                sleep(0.1)





        #add a word to the list
        elif command == 6:

            #if there is no vocab list to look in
            if not vocabulary:
                print('No vocab list')
                continue


            what_word = input("Word to add: ")

            #no empty words
            if not what_word.strip():
                print('No empty words')
                continue
            

            print(vocabulary.add_word(what_word))





        #add example for a word
        elif command == 7:

            if not vocabulary:
                print('No vocab list')
                continue

            mainword = input("Example for what word? ")
            print()

            #if word is in list
            if vocabulary.search_for_word(mainword):

                addcount = 0

                #allow user to type examples until they press enter
                while (example := input('Type the example (blank to stop): ')).strip().replace(' ', ''):
                    print(vocabulary.add_example(mainword, example), '\n')
                    addcount += 1

                
                print(f'{addcount} examples added for {mainword}')
            
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




        #empties list; debugging feature
        elif command == 10:

            if vocabulary:
                vocabulary = None
                print('List cleared')
            else:
                print('No vocab list')





if __name__ == "__main__":


    #program crashes if one CTRL + C out of the program unless I include an except case
    try:
        program()

    except KeyboardInterrupt:
        print('\nProgram exited through keyboard interrupt')