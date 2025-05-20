class Word:

    '''stores the name and examples for a word as parsed from a docx file'''


    def __init__(self, name: str):
        self.__name = name
        self.__examples = []
    


    @property
    def name(self):
        return self.__name



    def add_example(self, example: str):
        self.__examples.append(example)

    

    def __str__(self):
        return f'{self.__name.upper()}:\n{"\n".join(self.__examples)}'






class VocabList:

    '''stores and processes list of Word objects'''



    def __init__(self, vocablist: list):
        self.__vocablist = vocablist
    



    def __str__(self):
        
        return '\n\n'.join(str(word) for word in self.__vocablist)




    def add_word(self, new_word: str):

        #if word is not a duplicate
        if new_word not in [word.name for word in self.__vocablist]:
            self.__vocablist.append(Word(new_word))

        else:
            print('Word already in record')
    



    def add_example(self, word_name: str, new_example: str):

        for word in self.__vocablist:
            if word.name.lower() == word_name.lower():
                word.add_example(new_example)
                return
        

        print('word not found')




    #returns the entry for the word you search

    def search_for_word(self, which_word: str):

        #if a match exists
        if (match := list(filter(lambda word: word.name.lower() == which_word.lower(), self.__vocablist))):
            return(str(match[0]))
        
        #if a match was not found
        else:
            return(f'word not found')




    #deletes word from list

    def delete_word(self, word2del: str):


        #word is object of class Word

        for word in self.__vocablist:
            if word.name.lower()  == word2del.lower():
                self.__vocablist.remove(word)
                return f'{word2del} deleted from list'

        return "word not found"







if __name__ == "__main__":

    nothing = Word('nothing')

    nothing.add_example('what a bloody good time')
    nothing.add_example('test2')



    blah = Word('blah')

    blah.add_example('idk waht')
    blah.add_example('things')


    yo = Word('yo')

    yo.add_example('ya boi')



    alist = VocabList([nothing, blah, yo])
    print(alist.search_for_word('blah'))