""" fName = input("Enter your first name: ")
mName = input("Enter your middle name: ")
lname = input("Enter your last name: ")

#chain method
fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lname = lname.strip().capitalize()

print(f"Hello {fName}.{mName:.1s} {lname}, Welcome to python world")

print("="*50)
 """
###################################################################

########################
# Slice Email
########################

name = input("Enter your name: ").strip().capitalize()
email = input("Enter your mail: ").strip()

userName = email[ :email.index("@")]
emailDomin = email[email.index("@") + 1 : ]

print("="*50)
print(f"Hello {name}, your mail is: {email}")
print(f"your username: {userName}\nAnd your domain: {emailDomin}")
