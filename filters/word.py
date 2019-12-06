#This method finds common english words in potential secrets

def word(suspect):
    with open('filters/words/list.txt', 'r') as wordList:
        listOfWords = wordList.read().split('\n')
        for item in listOfWords:
            if(item in suspect):
                wordList.close()
                return True
        wordList.close()
        return False
        