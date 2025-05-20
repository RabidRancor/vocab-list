from docx import Document
from json import dump



def word_to_list(filename: str):

    '''Extracts content from the docx file (filename) and converts it to a list of dictionaries'''

    finaloutput = []

    current_word = ""
    current_examples = []


    #our file read object
    doc = Document(filename)


    #each paragraph in the document
    for paragraph in doc.paragraphs:
        
        #extract the paragraph as a string with newline/carriage return removed
        text = paragraph.text.strip()

        #empty paragraph is ignored
        if not text:
            continue


        bold = False


        #check the runs in this paragraph for any bold
        #if it detects a bold run, immediately sets the bold flag to True
        #and stops searching the paragraph

        for run in paragraph.runs:
            if run.bold:
                bold = True
                break



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





def list_to_json(vocablist: list, outputfile: str = 'vocab.json'):

    #utf-8 is cross compatible

    with open(outputfile, 'w', encoding = 'utf-8') as j:


        #ensure ascii can help with accented or special unicode characters
        #indentation used so the .json file is readable

        dump(vocablist, j, ensure_ascii = False, indent = 2)






if __name__ == '__main__':
    filename = input('Which file to access: ')
    
    list_to_json(word_to_list(filename))