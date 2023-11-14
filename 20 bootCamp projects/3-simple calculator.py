####################################################################################
# Author: Walid Omar
# Brief: Basic calculator script in Python. Defines arithmetic functions (addition,
#        subtraction, multiplication, division). Takes user input for two numbers
#        and operation choice. Performs the chosen operation and prints the result.
#        Includes error handling for invalid input.
####################################################################################

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    
    if num2 == 0:
        raise ValueError ("Second Operand must be larger than '0'")
    else:
        return num1 / num2
    
def calculator(num1, num2, operation):
    match operation:
        case 'add' | '+': return add(num1, num2)
        case 'sub' | '-': return sub(num1, num2)
        case 'mul' | '*': return mul(num1, num2)
        case 'div' | '/': return div(num1, num2)

try:
    number1 = float(input("Enter the First number: "))
    number2 = float(input("Enter the Second number: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit(1)
    
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ").strip()

if choice == '1':
    operation = 'add'
elif choice == '2':
    operation = 'sub'
elif choice == '3':
    operation = 'mul'
elif choice == '4':
    operation = 'div'
else:
    print("Invalid choice.")
    exit(1)

result = calculator(number1, number2, operation)
print(f"the result= {result}")


