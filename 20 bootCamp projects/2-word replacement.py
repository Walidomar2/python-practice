
str = input("Enter your string: ").strip()

def wordReplacement(sentence):
    
    wordToReplace = input("Enter the word you want to replace: ").strip()
    
    word = input("Enter the replacement word: ").strip()
    
    print(f"the new sentence is : {sentence.replace(wordToReplace, word)}")
    

wordReplacement(str)

    
    