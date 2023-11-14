
print("This is monthly payment loan calculator \n")

loanAmount = float(input("Enter the loan amount: "))
apr = float(input("Enter the annual interest rate: "))
years = int(input("Enter the amount of years: "))

monthlyInterestRate = apr / 1200
amountOfMonths = years * 12
monthlyPayment = loanAmount * monthlyInterestRate / (1- (1 + monthlyInterestRate) ** (- amountOfMonths))

print(f"the monthly payment= {monthlyPayment:0.2f}$")


