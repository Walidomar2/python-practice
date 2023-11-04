###########################################
# Files Handling

# 1) 'a' Open file for appending values, create file if not exists'
# 2) 'r' Read from file and give Error if file isn't exists [Default Value]
# 3) 'w' Writing in the file, create it if not exists
# 4) 'x' create file, give error if the file exists
##########################################

""" import os 

#Main Current Working Directory
print(os.getcwd())  #D:\courses\Python

#full path of the opened file 
print(os.path.abspath(__file__))    #d:\courses\Python\codes\files.py

#directory for the opened file
print(os.path.dirname(os.path.abspath(__file__))) #d:\courses\Python\codes

#changing Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__))) #d:\courses\Python\codes
print(os.getcwd())

# if you have a folder start with n and you can't write \n

file = open(r"d:\courses\Python\codes\nfolder\walid.txt")
 """

file = open("d:\courses\Python\codes\walid.txt","r")

#print(file) #File Data Object it store Info about the file not that containt 

#print(file.name)
#print(file.mode)
#print(file.encoding)

print(file.read()) #you can enter the number of char that u want to read and the default value is -1 so it can read all 
file.close()

#print(file.readline()) # you can enter the number of char u want to read from the line and the default value will read the whole line

""" list_1= file.readlines()
print(list_1) """


print("="*50+'\n')
file = open("d:\courses\Python\codes\walid.txt","r")

for line in file:
    print(line)

    if line.startswith("P"):
        break;
















