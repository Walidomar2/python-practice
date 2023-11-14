####################################################################################
# Author: Walid Omar
# Brief: A Python script that takes a user input email address, parses it into
#        username, domain, and extension, and prints the extracted components.
#        Assumes a valid email format with '@' and '.' separators.
####################################################################################

userEmail = input("Enter the email: ").strip()

(userName, domain) = userEmail.split('@')
(domain, extention) = domain.split('.')

print(f'userName  ==> {userName}')
print(f'domain    ==> {domain}')
print(f'extention ==> {extention}')

# You can do it with Regular Expressions too