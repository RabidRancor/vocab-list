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
        examples = "\n- ".join(self.__examples)
        return f'{self.__name}:\n- {examples}'





class VocabList:

    '''stores and processes list of Word objects'''


    def __init__(self, vocablist: list):
        self.__vocablist = vocablist
    



    #allows one to sort through a VocabList like a regular list
    def __iter__(self):
        return iter(self.__vocablist)




    #gets number of words
    def __len__(self):
        return len(self.__vocablist)





    #apparently makes my list subscriptable
    #so i cant iterate through it in indexed fashion
    def __getitem__(self, index):
        return self.__vocablist[index]




    #prints the list with big gaps between words
    def __str__(self):
        
        body = '\n\n\n'.join(str(word) for word in self.__vocablist)
        count = len(self.__vocablist)
        return body





    def add_word(self, new_word: str):
        '''add a Word object to the VocabList'''

        #if user inputs blank word
        if not new_word.strip():
            return 'Empty field, no word added'


        #if word is not in list already
        if not self.search_for_word(new_word):

            self.__vocablist.append(Word(new_word))
            return f'Added {new_word} to list'
        
        
        return 'Word already in list'

    



    def add_example(self, word_name: str, new_example: str):
        '''add an example to the Word object with matching name'''

        searchword = self.search_for_word(word_name)
        searchword.add_example(new_example)
        return f'Example added for {word_name}'
        





    #returns the reference to the word you searched (if it exists)
    #handles all the case sensitivity for the VocabList

    def search_for_word(self, which_word: str):
        '''search for word (case insensitive) in list and return its object'''


        #uses a generator comprehension to only generate for words where the word matches the input word
        #if it's not detected, it returns a None
        #next essentially iterates the generator a single time

        return next((word for word in self.__vocablist if word.name.lower() == which_word.lower()), None)






    #deletes word from list

    def delete_word(self, word2del: str):
        '''delete word from VocabList'''


        if not word2del.strip():
            return 'Empty field, nothing deleted'


        searchword = self.search_for_word(word2del)  
        self.__vocablist.remove(searchword)
        return f'{word2del} removed from list'






