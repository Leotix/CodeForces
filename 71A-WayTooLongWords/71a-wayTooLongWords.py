def shortenWords():
    numOfWords = int(input())
    wordsList = []
    for i in range(numOfWords):
        wordsList.append(input())
        wordLength = len(wordsList[i])
    for word in wordsList:
        if(len(word) > 10):
            print(f"{word[0]}{len(word[1:-1])}{word[-1]}")
        else:
            print(word)
 
if __name__ == "__main__":        
    shortenWords()
