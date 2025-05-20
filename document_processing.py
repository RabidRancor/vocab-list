from docx import Document
import json



def word_to_list(files: list):

    '''Extracts content from arbitrary amount of docx files and converts it to a list of dictionaries'''

    finaloutput = []

    #file = file name from a list of file names
    for file in files:


        #our file read object
        doc = Document(file)


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
            #bold is a boolean flag
            #if it detects any bolded runs, it outputs a True


            bold = any(run.bold for run in paragraph.runs)



            #if the paragraph is bold text
            if bold:


                #if the current line is a bold one
                #and there is a value already in current_word
                #then that means you're onto the next word and should upload
                #the previous word and examples to the list

                #this is only triggered when you reach the second word and onwards

                if current_word:

                    finaloutput.append({'word': current_word, 'examples': current_examples})

                

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


        finaloutput.append({'word': current_word, 'examples': current_examples})

    return finaloutput





def list_to_json(vocablist: list, filename: str = 'vocab.json'):

    '''creates a json file populated with contents of a list of dictionaries'''


    #utf-8 is cross compatible

    with open(filename, 'w', encoding = 'utf-8') as j:


        #ensure_ascii can help with accented or special unicode characters
        #indentation used so the .json file is readable

        json.dump(vocablist, j, ensure_ascii = False, indent = 2)






def json_to_list(filename: str = 'vocab.json'):

    with open(filename, 'r', encoding = 'utf-8') as f:
        return json.load(f)