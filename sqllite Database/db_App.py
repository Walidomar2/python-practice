##############################################################
# python + SQLlite App
##############################################################

import sqlite3


# A function to check whither id in the DB or not

def idchecker(id):
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    
    cr.execute("SELECT userID from skills")
    idList = cr.fetchall()
    
    idResult = []
    for item in idList:
        idResult.append(item[0])
    
    print(idResult)
    if id in idResult:
        print("User Found.. \n")
        return True
    else:
        print("User Not found...")
        return False

# show skills function
def showSkills(id):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        
        cr.execute(f"SELECT skill,progress FROM skills WHERE userID = {id}")
        result = cr.fetchall()
        
        print(f"there are {len(result)} skills in your TABLE")
        
        for num,skill in enumerate(result):
          print(f"{num} ==> {skill[0]} with progress = {skill[1]}")
    except sqlite3.Error:
        print(f"ERROR ==> {sqlite3.Error}")
        
    finally:
        db.close()

# Add new skill function
def addSkill(id):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        
        newSkill = input("Enter the new skill row [skill - progress]: ").split()
        
        cr.execute(f"INSERT INTO skills (skill, progress,userID) VALUES ('{newSkill[0]}', {newSkill[1]},{id})")
        
        db.commit()
    except sqlite3.Error:
        print(f"ERROR ==> {sqlite3.Error}")
        
    finally:
        db.close()
    
# Delete a skill function
def deleteSkill(id):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        
        skill = input("Enter the skill you want to delete [skill]: ")
        
        cr.execute(f"DELETE FROM skills WHERE skill = '{skill}' AND userID = {id}")
        db.commit()
        
    except sqlite3.Error:
        print(f"ERROR ==> {sqlite3.Error}")
        
    finally:
        db.close()

# Update skill function
def updateSkill(id):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        
        skill = input("Enter the skill you want to update [skill]: ")
        newSkill = input("Enter the new skill [skill - progress]: ").split()
        
        cr.execute(
            f"UPDATE skills SET skill = '{newSkill[0]}', progress = {newSkill[1]} WHERE skill = '{skill}' AND userID = {id}")
        db.commit()
        
    except sqlite3.Error:
        print(f"ERROR ==> {sqlite3.Error}")
        
    finally:
        db.close()
    

# A command list to check the user option
commandList=['s', 'a', 'd', 'u', 'q']

# the main message for the user 
inputMessage = """
*********************** Welcome to skills DB mini project ********************

What Do You Want To Do ?
"s" => Show All Skills 
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: 
"""

# taking the userID from user
uid = int(input("Enter your ID: ").strip())

if idchecker(uid):

    while True:
        # taking the user option 
        userOption = input(inputMessage).strip().lower()

        # check if the user option not in command list 
        if userOption not in commandList:
            print("Please enter a correct option")

        match(userOption):
            case 's': showSkills(uid)
            case 'a': addSkill(uid)
            case 'd': deleteSkill(uid)
            case 'u': updateSkill(uid)
            case 'q': break
        

    print("DB program CLOSED.....")
else:
    print("Enter right ID")
    

    

