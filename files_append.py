file = open("d:\courses\Python\codes\walid.txt",'w')


#it will clear all the old containt and writing
#file.write("Writing from VScode Test")
#file.write("Writing from VScode second Test")

file = open(r"d:\courses\Python\codes\file_2.txt",'w')
file.write("Hi Here\n"*20)

# 2) file.writelines(list_of_lines)

# Append 
# it will writing without clearing anything 

file.close()

file = open(r"d:\courses\Python\codes\file_2.txt",'a')
file.write("Test Here\n")

tempList = []
resultList = []
tempList.append("walid")
tempList.append(5.2)

resultList.append(tempList)

print(resultList)


# tell()   ==> position of cursor
# truncate()
# seek(pos) ==>reading from a position u give

# os.remove("path")  ==> you can remove the file from it

