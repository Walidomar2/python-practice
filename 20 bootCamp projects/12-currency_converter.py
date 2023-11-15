########################################################################
# auther: Walid Omar
# brief:  A python script to change the currency from dollars to pounds
########################################################################

try:
    userDollars = float(input("Enter the amount of dollars: "))
except ValueError:
    print("Must enter numerical value")
    
#lambda function to convert the dollars to pounds 

currencyConverter = lambda dollars: dollars * 0.82

print(f"the equivalent of {userDollars}$ pounds= {currencyConverter(userDollars)}£")



