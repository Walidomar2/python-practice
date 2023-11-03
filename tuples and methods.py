###################################
# Facts about tuples :

# Tuples Items Are Enclosed in Parentheses
# You Can Remove The Parentheses 
# Tuples Allow Using Index To Access Items
# Tuples Are Immutable => you can't Add or Delete Items  
# Tuples Items Isn't Unique 
# Tuples Can Have Different Data Types 
# Operation Used in Strings & Lists Available In Tuples

##################################

myFirstTup = ("Walid", "Omar",)
mySecTup = "Khalaf","Mahmoud"

print(myFirstTup)
print(mySecTup)

print("="*50 + "\n")

#Tuple with One Element 

oneEleTup = "Walid"
print(type(oneEleTup))

oneEleTup = "Walid",
print(type(oneEleTup))
print(len(oneEleTup))

my_3thTuple= myFirstTup + mySecTup

print(my_3thTuple)

my_5thTuple = myFirstTup + (1,2,3) + mySecTup
print(my_5thTuple)

###############
# Methods 
##############

# 1) count()
# 2) index()
# 3) Destruct()

newTup = ("A", "B", 4,"C",)

var1,var2,_,var3 = newTup

print(var1)
print(var2)
print(var3)


var1,var2,var4,var3 = newTup
print(var4)












