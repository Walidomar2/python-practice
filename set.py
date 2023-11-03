####################################
# Facts about sets

# 1) Set Items Are Enclosed in Curly Braces
# 2) Set Items Aren't Ordered & not Indexed
# 3) Set Indexing And Slicing Can't be Done 
# 4) Set Has only Immutable Data Types (Number, Strings, Tuples) 
# 5) Set Items Is Unique
###################################


mySetOne = {1,2,3,4,5,6}
print(mySetOne)

mySetTwo = {1,1,2,2,"Walid","Walid"}
print(mySetTwo)

########################
# set Methods
#######################

# 1) clear()
# 2) union()  with another sets just in printing

mySetOne = {1,2,3,4,5,6}
mySetTwo = {7,8,9}

print(mySetOne | mySetTwo)
print(mySetOne.union(mySetTwo))

# 3) add() just one element in a time

mySetOne.add(7)
print(mySetOne)

# 4) Copy()
# 5) remove()  will remove the element but if the element not found will through error

# 6) discard() will remove the element but if the element not found won't through error 

mySetOne.discard(7)
print(mySetOne)

# 7) pop() will pop random element from the set 

print(mySetOne.pop())

# 8) update() same as union but it will update the set with the new element not just for printing

mySetOne.update(mySetTwo)
print(mySetOne)
mySetOne.update([20,50,30])
print(mySetOne)

# 9) difference() will show the different elements between two sets

mySetOne = {1,2,3,4,5,6}
mySetTwo = {7,8,9,1,5,6}

print(mySetOne.difference(mySetTwo))  # ==> print(mySetOne - MySetTwo)

# 10) difference_update() it will update the set with the difference elements

mySetOne.difference_update(mySetTwo)

print(mySetOne)

# 11) intersection() 

mySetOne = {1,2,3,4,5,6}
mySetTwo = {7,8,9,1,5,6}

print(mySetOne.intersection(mySetTwo))  # ==> print(mySetOne & mySetTwo)

# 12) intersection_update()

mySetOne.intersection_update(mySetTwo)
print(mySetOne)

# 13) symmetric_difference()

mySetOne = {1,2,3,4,5,6}
mySetTwo = {7,8,9,1,5,6}

print(mySetOne.symmetric_difference(mySetTwo)) # ==> mySetOne ^ mySetTwo

# 14) symmetric_difference_update()

# 15) issuperset()
mySetOne = {1,2,3,4,5,6}
mySetTwo = {7,8,9,1,5,6}
my3thSet = {1,2,4,5}

print(mySetOne.issuperset(mySetTwo))
print(mySetOne.issuperset(my3thSet))

# 16) issubset()

print(my3thSet.issubset(mySetOne))
print(mySetOne.issubset(my3thSet))

# 17) isdisjoint()

print(mySetOne.isdisjoint(mySetTwo))  # False because they are have some same elements so there is joint between them





