#####################################
######## Function & Return #########
####################################


""" def sayHello(name):
    print(f"Hello {name.strip().capitalize()}")


sayHello("                     Walid")

print("="*50 +"\n")

def addFun(num_1,num_2):
    return num_1 + num_2

sum = addFun(50 , 10)
print(sum) """

def print_student_skills(student_list):

    
    for student, skills in student_list.items():
        print("=" * 50)
        print(f"The skills of {student} Are: ")
        
        for skill, progress in skills.items():
            print(f"-{skill} with progress= {progress}")

# Define your list of students and their skills
students = {
    "Walid": {
        "C": "95%",
        "C++": "80%",
        "python": "90%"
    },
    "karem": {
        "Cloud": "95%",
        "Backend": "90%",
        "docker": "80%"
    },
    "Mohamed": {
        "python": "90%",
        "HTML": "95%",
        "CSS": "95%"
    }
}

print_student_skills(students)