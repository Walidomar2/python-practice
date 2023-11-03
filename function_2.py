""" def showSkills (name,*skills,**skillsWithPro):
    print(f"{name} Skills Is:")

    print("First the skills without progress:")
    for skill in skills:
        print(f"- {skill}")
    
    print("Second The Skills With Progress:")
    for skillKey, SkillVal in skillsWithPro.items():
        print(f"- {skillKey} ==> {SkillVal}")


#showSkills("Walid",'ARM','AUTOSAR',python='95%',RTOS='80%')

mySkillsProg ={
    'Python'  : "95%",
    'RTOS'    : "95%"

}

mySkills = ('ARM','AUTOSAR')

showSkills("Walid",*mySkills,**mySkillsProg)

 """

###########################################
# Recursion Function Example
##########################################

""" def cleanWord(word):
    if len(word) == 1:
        return word
    
    if word[0] == word[1]:
        return cleanWord(word[1:])
    else:
        return word[0]+cleanWord(word[1:])

print(cleanWord("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiii"))
print(cleanWord("wwwwwwwwooooooooooooorldddddddddd")) """



####################################
# lambda function

# 1) It has no Name
# 2) You Can Call it Inline without Defining it 
# 3) You Can Use it in Return Data From Anothor Function
# 4) Used for simple functions and def handle the larg functions
# 5) one single expression not block of code
###################################

#name ="walid"

hello = lambda name: f"hello {name}"

print(hello("Walid"))






