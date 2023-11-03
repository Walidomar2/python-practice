###################################################
#Facts about dictionary

# 1) Items Are Enclosed in Curly Braces
# 2) Items Are Contains Key : Value
# 3) Key Need To Be Immutable => (Number, String, Tuple)
# 4) Value Can Have Any Data Types
# 5) Key Need To Be Unique 
# 6) You Can Access Elements by the Key 
###################################################

user ={
    "name"       : "Walid",
    "age"        : 26,
    "country"    : "Egypt",
    "Skills"     : ["C programming","C++","python"]
}

#print(user)        #will show all the dictionary key : values

#Two ways to access An Element 
print(user["name"])
print(user.get("name"))

# To show all the dic Keys
print(user.keys())

# To show all the dic Values
print(user.values())

# 2D- dic
lang ={
    "One" : {
        "name" : "python",
        "progress" : "80%"
    },

    "Two" : {
        "name" : "C",
        "progress" : "95%"
    }
}

print(lang["One"])
print(lang["One"]["name"])

# To know the number of keys in dic 
print(len(user))

print(len(lang["One"]))

# Create Dic From Variables 

One = {
    "name" : "python",
    "progress" : "80%"
    }

Two ={
    "name" : "C",
    "progress" : "95%"
    }

langua = {
    "First" : One,
    "Second" : Two
}

print(langua)
print(langua['First']['name'])

print("="*50 +'\n')

#########################
# Methods 
#########################

# 1) clear()

# 2) update()

#there is two ways for updating

dic_1 ={
    "name" : "Walid"
}

print(dic_1)

dic_1["age"] = 36
print(dic_1)

dic_1.update({"country" : "Egypt" , "skilles" : "python"})
print(dic_1)

print("="*50 +'\n')


# 3) copy()

# 4) keys()
# 5) values()

# 6) setdefault()    => if there's no value for a key you can make a default value for it

dic_1.setdefault("password" , "0000")
print(dic_1)

# 7) popitem() => pop the last element you put in dictionary 

print(dic_1.popitem())

# 8) items() => will store the items in a copy and changes will be applied in that copy every time

user_2 = {
    "name" : "walid",
    "age" : 37
}

var_1 = user_2.items()
print(var_1)

user_2["country"] = "Egypt"

print(var_1)


# 9) fromkeys()

a = ("myKeyOne", "myKeyTwo", "myKeyThree")
b = "none"

print(dict.fromkeys(a,b))

dic_2 = dict.fromkeys(a,b)
print(dic_2)

