#########################################################
# Modules  ==> like library in C 

# 1) Module is a file contain a set of functions
# 2) You can Import module in your App to help you 
# 3) You can Import Multiple Modules
# 4) You Can Create Your Own Modules
# 5) Modules Saves Your Time
#########################################################


""" import random

print(f"Random float number: {random.random()}") """

# To show all function inside module
#print(dir(random))

# to import just function or n fumction
""" 
from random import randint , random
print(f"{randint(10,100)}")
print(f"Random float number: {random()}")
 """

""" import module_test

module_test.sayHello("Walid") """

import pyfiglet , termcolor

print(termcolor.colored(pyfiglet.figlet_format("          WELCOME w.o"), color = 'yellow'))

