
# 1) search() ==> return the first match only
# 2) findall() ==> returns a list of all matches and empty list if no match

import re


# Regular Expression to match => (E-l-z-e-r-o)
my_string = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
result = re.findall(r"(\w )", my_string)

print(result)       # ['E ', 'l ', 'z ', 'e ', 'r ', 'o ']

print("="*50)
# Regualr Experssion for a valid Email

userEmail = input("Enter your email ").strip()

result = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)",userEmail)

emailList = []

if result != []:
    print("Valid Email")
    emailList.append(result)
else:
    print("WARNNING: Not a valid Email")

print("="*50)

my_string1 = "+(0100) 600-1234"
my_string2 = "+(0100) 60-1234"
my_string3 = "(0100) 6000-1234"
my_string4 = "01006001234"
my_string5 = "0100 600 1234"
my_string6 = "(0100) 600-1"
my_string7 = "(0100) 600-12"


result1 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string1)
result2 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string2)
result3 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string3)
result4 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string4)
result5 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string5)
result6 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string6)
result7 = re.findall(r"((\+?)(\(0100\))\s(\d{,4})-(\d{4}))", my_string7)



print(result1)
# ['+(0100) 600-1234']
print(result2)
# ['+(0100) 60-1234']
print(result3)
# ['(0100) 6000-1234']
print(result4)
# []
print(result5)
# []
print(result6)
# []
print(result7)
# []


print("="*50)

my_string1 = "http://www.elzero.org:8888/link.php"
my_string2 = "https://elzero.org:8888/link.php"
my_string3 = "http://www.elzero.com/link.py"
my_string4 = "https://elzero.com/link.py"
my_string5 = "http://www.elzero.net"
my_string6 = "https://elzero.net"

result1 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string1)
result2 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string2)
result3 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string3)
result4 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string4)
result5 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string5)
result6 = re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))", my_string6)


print(result1)
# ['http://www.elzero.org:8888/link.php']
print(result2)
# ['https://elzero.org:8888/link.php']
print(result3)
# ['http://www.elzero.com/link.py]
print(result4)
# ['https://elzero.com/link.py]
print(result5)
# []
print(result6)
# []

print("="*50)

# Regular Expression to match => (http || https) by 5 methods.

# RegEx. 1 => https?
# RegEx. 2 => http\w?
# RegEx. 3 => http.?
# RegEx. 4 => http[a-z]?
# RegEx. 5 => http\S?

import re

my_string = "http || https || abcd || abcd"

result = re.findall(r"(http\w?)", my_string)

print(result)
#['http', 'https']