import datetime

print(f"{datetime.datetime.now()} \n")

print(datetime.datetime.now().strftime("%Y-%m-%d"))
print("="*50)

print(datetime.datetime.now().strftime("%d-%b-%Y"))
# 01-Jul-2022
print("="*50)

print(datetime.datetime.now().strftime("%d/%b/%y"))
# 01/Jul/22
print("="*50)

print(datetime.datetime.now().strftime("%a, %d %B %Y"))
# Fri, 01 July 2022
print("="*50)

print(datetime.datetime.now().strftime("%x"))
# 07/01/22
print("="*50)


year = int(input("Enter your birth year"))
month = int(input("Enter your birth month"))
day = int(input("Enter you birth day"))

birthDate = datetime.datetime(year,month,day)
currentDate = datetime.datetime.now()

age = currentDate - birthDate

years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30  # Using an approximate value for months
days = remaining_days % 30

print(f"Your age = {years} Years, {months} Months, and {days} Days")