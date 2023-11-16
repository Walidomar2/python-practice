
 
from abc import ABCMeta, abstractmethod

class programming(metaclass = ABCMeta):
    
    @abstractmethod
    def hasOOP(self):
        pass
    

class python(programming):
    def hasOOP(self):
        print("Yes, python has OOP")

class pascal(programming):
    
    def hasOOP(self):
        print("NO, pascal has no OOP")
        



progObject = python()
progObject2 = programming()     #It will give error because it's abstracted class just like pattern class for derived classes 

progObject.hasOOP()
    
     
    
    
