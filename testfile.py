from document_processing import word_to_list, list_to_json


    
files = []
while (userchoice := input("Add .docx files to convert to .json (blank to stop inputting): ")):
    files.append(userchoice)

json_file_name = input("What do you want the .json to be called? ").strip()

list_to_json(word_to_list(files), json_file_name)