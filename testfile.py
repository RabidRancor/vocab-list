from document_processing import word_to_list, list_to_json




def help():

    commands = ['\nCommands:', '(0) exit', '(1) reprint help' ,'(2) docx => json', '(3) search by word']

    for line in commands:
        print(line)



def program():

    help()

    #only accepts numerical inputs
    #0 ends the program

    while (command := int(input('\ncommand: '))) != 0:
        
        if command == 1:

            help()
        


        elif command == 2:

            files = []
            while (docxfile := input("Add .docx files to convert to .json (blank to stop inputting): ")):
                files.append(docxfile)

            json_file_name = input("What do you want the .json to be called? ").strip()

            list_to_json(word_to_list(files), json_file_name)
        


        elif command == 3:

            searchword = input("What word are you looking for? ")


            files = []
            while (docxfile := input("Choose .docx files to search from (blank to stop inputting): ")):
                files.append(docxfile)


            matchfound = False

            for word in word_to_list(files):
                if word["word"] == searchword:
                    print(word)
                    matchfound = True
                    break

            if not matchfound:
                print('no matches')




if __name__ == "__main__":
    program()