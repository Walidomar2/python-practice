####################################################################################
# Author: Walid Omar
# Brief: A Python script for generating random passwords. The script utilizes the 
#        'random' and 'string' modules to create strong and unpredictable passwords.
#        Users can specify the desired password length, and the script generates a
#        password composed of a mix of uppercase and lowercase letters, digits, and
#        special characters.
####################################################################################


import random
import string

charactersList = list(string.ascii_letters + string.digits + "@#$%&*")

def generatePassword():
    try:
        passwordLen = int(input("Enter the password length: "))
    except ValueError:
        print("password length must be numerical value")

    random.shuffle(charactersList)
    
    password = []
    for i in range(passwordLen):
        password.append(random.choice(charactersList))
        
    password = ''.join(map(str,password))    # Convert the list of characters into a string
    
    return password

while True:
    answer = input("Do you want to generate a password(Y/N): ").strip().capitalize()
    
    if answer == 'Y':
        generatedPassword = generatePassword()
        print(f"your new password is {generatedPassword}")
        
        pass
    else:
        
        break
    
    