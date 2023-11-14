####################################################################################
# Author: Walid Omar
# Brief: Python implementation of binary search algorithm. Assumes the input list
#        is sorted. The function takes a sorted list and a target element, and it
#        returns the index of the target element if found, otherwise returns -1.
####################################################################################

numberList = [1,2,3,4,7,8,2,4,6,10] #[1,2,2,3,4,4,6,7,8,10]

try:
    targetElement = int(input("Enter the element you want to search: "))

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit(1)

def binarySearch(lis,number):
    lis.sort()
    rightIndex = len(lis) - 1
    leftIndex = 0
    midIndex = 0

    
    while leftIndex <= rightIndex:
        midIndex = int((leftIndex + rightIndex) / 2)
        
        if number == lis[midIndex]:
            return midIndex
        elif number > lis[midIndex]:
            leftIndex = midIndex + 1
        else:
            rightIndex = midIndex - 1
    
    return "Not found"


resultIndex = binarySearch(numberList, targetElement)

if resultIndex == 'Not found':
    print(resultIndex)
else:
    print(f"The index of the target value in the Sorted list is: {resultIndex} ")
            

