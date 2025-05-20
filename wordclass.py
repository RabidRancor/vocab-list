'''Module containing class definitions for Word and VocabList'''



class Word:

    '''Stores the name and examples for a word'''


    def __init__(self, name: str):
        self.__name = name
        self.__examples = []
    


    @property
    def name(self):
        return self.__name
    


    @property
    def examples(self):
        return self.__examples



    #allows one to directly convert a dictionary into a Word object
    #useful for converting json to VocabList
    @classmethod
    def from_dict(cls, orig: dict):
        
        #create a Word objet with name attribute from the dictionary
        word = cls(orig["word"])

        #get accesses the contents for a given key
        #the second parameter is the fallback output

        #we use add_example rather than directly exposing the examples attribute
        #so you can create a word without examples

        for example in orig.get("examples", []):
            word.add_example(example)


        return word




    def add_example(self, example: str):
        '''add an example to Word object'''
        
        self.__examples.append(example)

    


    def __str__(self):
        return f'{self.__name.upper()}:\n- {"\n- ".join(self.__examples)}'





class VocabList:

    '''stores and processes list of Word objects'''



    def __init__(self, vocablist: list):
        self.__vocablist = vocablist
    


    #allows one to sort through a VocabList like a regular list
    def __iter__(self):
        return iter(self.__vocablist)



    def __str__(self):
        
        body = '\n\n\n'.join(str(word) for word in self.__vocablist)
        count = len(self.__vocablist)
        return f"{body}\n\n\n-----\nWords: {count}"




    def add_word(self, new_word: str):
        '''add a Word object to the VocabList'''

        #if word is not a duplicate
        if new_word not in [word.name for word in self.__vocablist]:
            self.__vocablist.append(Word(new_word))

        else:
            print('Word already in record')
    



    def add_example(self, word_name: str, new_example: str):
        '''add an example to the Word object with matching name'''

        for word in self.__vocablist:
            if word.name.lower() == word_name.lower():
                word.add_example(new_example)
                return
        

        print('word not found')




    #returns the entry for the word you search

    def search_for_word(self, which_word: str):
        '''search for word (case insensitive) and return its contents'''

        #if a match exists
        if (match := list(filter(lambda word: word.name.lower() == which_word.lower(), self.__vocablist))):
            return(str(match[0]))
        
        #if a match was not found
        else:
            return(f'word not found')




    #deletes word from list

    def delete_word(self, word2del: str):
        '''delete word (case insensitive) from VocabList'''

        #word is object of class Word

        for word in self.__vocablist:
            if word.name.lower()  == word2del.lower():
                self.__vocablist.remove(word)
                return f'{word2del} deleted from list'

        return "word not found"





