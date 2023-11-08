def generatorTest():
    yield "walid"
    yield  [1,2,3,4,5]


genObject = generatorTest()

print(next(genObject))
print(next(genObject))

print("="*50 +"\n")
###########################################################################################
# Decorators

# Decorator Take A function and add some functionality  and Return it 
# Decorator Warp Other Function And Enhance Their behaviour
# Decorator is Higher Order Function (That Can accept function as parameter)
###########################################################################################

# Function Execution Time 


from time import time

def decorator_1(func) :

    def nestedFun(na):

        startTime = time()
        func(na)
        endTIme = time()

        print(f"The sayHello Function Execution time = {endTIme - startTime}")

    return nestedFun
    
@decorator_1
def sayHello(name):
   print(f"Hello {name.strip().capitalize()}")

@decorator_1
def sayHelloIteration(name):
    for i in range(0,2000000):
        
        if i == 199 or i == 1000:
            print(f"Hello {name.strip().capitalize()}")
    

sayHello('walid')
sayHelloIteration('walid')

dic = {}
list = [1,2,3,4,5,6,7]

dic ["walid"] = list        # it will makes walid as key and the list as value

print(dic['walid'])


