####################################################################################
# Author: Walid Omar
# Brief: A Python script that takes a user input string and performs a word
#        replacement. The user is prompted to enter a word in the given string
#        that they want to replace and the replacement word. The script then
#        prints the modified sentence with the specified replacement.
####################################################################################


str = input("Enter your string: ").strip()

def wordReplacement(sentence):
    
    wordToReplace = input("Enter the word you want to replace: ").strip()
    
    word = input("Enter the replacement word: ").strip()
    
    print(f"the new sentence is : {sentence.replace(wordToReplace, word)}")
    

wordReplacement(str)

    
    