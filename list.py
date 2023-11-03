#facts about lists

#############################################

# it's just items are enclosed in square brackets
# lists are ordered, to use index to access item 
# list are mutable => add,delete,edit
# list's items isn't unique 
# list can havee different data types

#############################################


myList = ["One", "Two", "Three", 1, 2, 2]

print(myList)
print(myList[3])
print(myList[-1])       #last element
print(myList[-3])

print(myList[1:4])

print(myList[::1])
print(myList[::2])


myList[0:3] = ["A", "B", "C"]
print(myList)

#myList[0:3] =[]
#print(myList)

myList[0:3] = ["A"]
print(myList)
print("-"*50 +"\n")
####################################################################

######################
# List Methods 
######################

#append() ==> you can add element/list to the list 

myNewList = ["Walid", "Omar", "Khalaf"]
myOldList = ["Mohamed",1,2,3]
print(myNewList)
myNewList.append("Mahmoud")
print(myNewList)

myNewList.append(myOldList)
print(myNewList)

print(myNewList[4][1])      #when u append two lists it act as 2D array

#extend() ==> you can add elements from a list to another list 

listNumbes1 = [1,2,3,6]
listNumbes2 = [4,5,6]

listNumbes1.extend(listNumbes2)

print(listNumbes1)

#remove ==> you can remove an element from list

listNumbes1.remove(6)

print(listNumbes1)

#sort() ==> ordering the elements but elements must be same data type

list2 = [1,2,9,7,8,3,5]
list2.sort()        #reverse by default = False
print(list2)

list2.sort(reverse=True)
print(list2)

#reverse()

list3 = [1,2,9,7,8,3,5,'A',6,'B']

list3.reverse()
print(list3)


#clear ==> removing all items

list3.clear()
print(list3)

#copy

list4 = list2.copy()
print(list4)


#count
list4 = [1,2,1,5,8,9,1,1,1]
print(list4.count(1))


#index
print(list4.index(9))



#insert ==> adding an element to before any position 
list4.insert(1,5)
print(list4)

#pop ==>removing an item and return the item 

print(list4.pop(6))






