

""" 
num = 0
while num < 10 :
   # print(num, end=' ' )
    print(str(num + 1).zfill(2))
    num += 1
    

else :
    print("\n"+"loop ended")
 """

""" list_1 = [1,2,3,4,5,6,7,8,9,10,11,12]

for number in list_1:
    print(number)
     """

""" mySkills = {
    "C "     : "90%",
    "C++"    : "80%",
    "python" : "80%"
}

for skill in mySkills:
    print(f"my progress in language {skill} programming = {mySkills[skill]}")
 """

students ={
    "Walid":{
        "C"     : "95%",
        "C++"   : "80%",
        "python": "90%"
    },
    "karem":
    {
        "Cloud"  : "95%",
        "Backend": "90%",
        "docker" : "80%"
    },
    "Mohamed":
    {
        "python" : "90%",
        "HTML"   : "95%",
        "CSS"    : "95%"
    }
}

print("="*80)

for student in students:
    print(f"The skills of {student} Are: ")

    for skill in students[student]:

        print(f"-{skill} with progress= {students[student][skill]}")
    print("="*80)







