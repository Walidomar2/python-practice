# 1) all() ==> check if all elements is true or not




list_1 =[1, 2, 0, 4]

if all(list_1):
    print("all is true")
else:
    print("false")


# 2) any() ==> check if there is at least one element is True

list_1 =[1, 2, 0, 4]

if any(list_1):
    print("true")
else:
    print("false")

# 3) bin() convert decimal number to binary 

print(bin(3))

# 4) id() ==> to get the address of the variable

a = 5
print(id(a))

# 5) sum(iterable,start)

listNum = [1,2,5,7]
print(sum(listNum))

print(sum(listNum,30))

# 6)round(number ,numofdigits)

print(round(105.621))
print(round(105.536,2))

# 7)range(start,end,step)
list_1 = list(range(2,20,2))
print(list_1)

# 8) abs(num) ==> return the positive value only

# 9) pow(base,exp,mod) ==> power of the number base**exp

print(pow(2,5))  # mod parameter ==> not a must 
print(pow(2,5,10)) # ==> 32 % 10 = 2

# 10) min() ==> return the minimum item between items

print(min(1,-10,2,3,5))

# 11) max()

# 12) slice(start,end,step)


##################################
# Map() ==> Take a function (def function or lambda)+ iterator
#################################

""" def formatedText(name):
    return f"- {name.strip().capitalize()} -"


names = ["WALID", "KAREM","MoHamed"]

for name in map(formatedText,names):
    print(name)


listNames = list(map(formatedText,names))
print(listNames)

 """

# with lambda



names = ["WALID", "KAREM","MoHamed"]

for name in map(lambda text: f"- {text.strip().capitalize()} -",names):
    print(name)


listNames = list(map(lambda text: f"- {text.strip().capitalize()} -",names))
print(listNames)


#######################################################################################

###############################################################
# Filter()

# 1) FIlter Take A function + iterator
# 2) Run a function on every element
# 3) The function can be Pre-Defined Function or lambda
# 4) Filter out all elements for which the function return true 
# 5) The function Need to Return Boolean Value 
##############################################################

def checkNumbers(num):
 # if num > 10 :
       # return num 
    return num > 10
    
numberList = [5,80,4,6,90,15,21]

returnedNumber = list(filter(checkNumbers,numberList))  # zeros won't return from filter anyway
print(returnedNumber)

###################################################################
# reduce()

# 1) Reduce Take A function + iterator
# 2) Run a function on First AND Second Element and give result
# 3) then Run function on result and third element
# 4) then Run function on result and 4th element and so on
# 5) Till one element (result) is left and this is the result of the reduce
# 6) the function Can be Pre-defined Function or lambda function
###################################################################
from functools import reduce

def sumNum(num1,num2):
    return num1 + num2

result = reduce(sumNum,numberList)
print(result)



# enumerate(iterable,start) ==> counter

names = ["WALID", "KAREM","MoHamed"]

namesCounter = enumerate(names)     # you can give a start of counting 

for counter,name in namesCounter:
    print(f"{counter} - {name}")        # you can ignore counter var but output will be (1, name)



print("="*50 + '\n')

# help() ==> desciption for any function you want to know 
# print(help(print))

#reversed(iterable)

name = "Walid"

#print(reversed(name))

for i in reversed(name):
    print(f"{i}",end='')



