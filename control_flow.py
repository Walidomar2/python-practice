#########################
# if elif else
########################

""" name    = input("Enter your name: ").strip().capitalize()
course  = "Python"
price   = 100
country = input("Enter your country: ").strip()

print("="*50 +"\n")
if country == "Egypt" or country == "egypt":
    print(f"Hello {name}, Because you are from \"{country.capitalize()}\"")
    print(f"The \"{course}\" price is ${price - 80}")

elif country == "Qatar" or country == "qatar":
    print(f"Hello {name}, Because you are from \"{country.capitalize()}\"")
    print(f"The \"{course}\" price is ${price}")

else:
    print(f"Hello {name}, Because you are from \"{country}\"")
    print(f"The \"{course}\" price is ${price - 40}")

print("="*50 +"\n") """
################################################################################################

countries_1 = ["Egypt", "KSA", "Kuwait", "Qatar"]
price_1 = 80

countries_2 = ["USA", "UK", "GER"]
price_2 = 150

price_3 = 200

userCountry = input("Enter your country: ").strip()

if userCountry in countries_1:
    print(f"Because you are from {userCountry}, the price = {price_1}")
elif userCountry in countries_2:
    print(f"Because you are from {userCountry}, the price = {price_2}")
else :
    print(f"Because you are from {userCountry}, the price = {price_3}")