####################################################################################
# Author: Walid Omar
# Brief: A simple quiz game. The script defines a dictionary
#        containing quiz questions and answers. The user is prompted with each
#        question, inputs their answer, and the script checks and scores the responses.
####################################################################################



quizDict = {
    'question1':{
        'question': "What's the capital of Palestine? ",
        'answer': 'Gaza'
    },
    
    'question2':{
        'question': "What's the capital of Egypt? ",
        'answer': 'Cairo'
    },
    'question3':{
        'question': "What's the capital of Italy? ",
        'answer': 'Roma'
    },
    'question4':{
        'question': "What's the capital of Spain? ",
        'answer': 'Madrid'
    }
}

maxScore = 4
userScore = 0

for key, value in quizDict.items():
    print(value['question'])
    
    answer = input("Answer: ").strip().capitalize()
    
    if answer == value['answer']:
        userScore+=1
        print("Correct Answer")
    
    else:
        print("Wrong Answer")
        
    print("")
        

print(f"Your score = {userScore} out of {maxScore}")


        




