print("="*50)

name = "Ali"
age = 22
country = "Egypt"

print(f'Hello {name}, How are you doing?' +
      f' Your age is \"{age}\" ' + f'Your country is:{country}')
print("="*50)

myString = "I love Python"
print(myString[8:11])  # yth
print(myString[8:13:2])  # yhn
print(myString[:5])  # I lov
print(myString[5:])  # e Python
print(myString[:])  # I love Python

print("="*50)


name = "#@#@Ali#@#@"
print(name.strip("#@"))  # Ali
print(name.lstrip("#@"))  # @#@Ali
print(name.rstrip("#@"))  # Ali#@#@
print(len(name))  # 11


myTitle = "i love 2d arrays"

print(myTitle.title())

print("="*50)

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

print("="*50)

msg = "I Love Python And, I Love Elzero Web School"

print(msg.count('Love'))

print("="*50)

name_one = "MoUstaFa"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

print("="*50)

myString = "I love Python"
print(myString.startswith("I"))     # True
print(myString.startswith("P"))  # False
print(myString.startswith("P", 7, 12))  # True

print("\n", myString.endswith("n"))     # True
print(myString.endswith("N"))  # False
print(myString.endswith("e", 2, 6))  # True


print("="*50)

myString = "I love python"

print(myString.find("p"))  # 7
print(myString.find("p", 0, 15))  # 7
print(myString.find("p", 0, 5))  # -1

print(myString.index("p"))  # 7
print(myString.index("p", 0, 15))  # 7
# print(myString.index("p", 0, 5))  # will through Error because the p not found

print("="*50)


############################################################################################################

name = "Walid"
age = 26
rank = 12

print("My name is : %s , my age is : %d and my rank is : %d" %(name , age , rank))
print("My name is :{:s} , my age is : {:d} and my rank is :{:f}".format(name, age, rank))

print("="*50)
############################################################################################################

a, b, c, = "one", "two", "three"

print("{} {} {}".format(a,b,c))
#print("{1} {2} {}".format(a,b,c))        //will give error "cannot switch from manual field specification to automatic field numbering"
print("{1} {2} {0}".format(a,b,c))
print("{1:s} {2:s} {0:s}".format(a,b,c))

print("="*50)
############################################################################################################
#pyformat.info          website as a resource for the formating in python
print(f"My name is :{name}, my age is :{age} and my rank is :{rank}")
