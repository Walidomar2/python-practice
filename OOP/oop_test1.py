############################################################################################################
# We have 3 types of methods: 

# 1) Instance Method ==> it takes at least 1 parameter (self)
# 2) class Method    ==> we must write @classmethod above it and it takes one parameter at least (cls)
# 3) static Method   ==> we must write @staticmethod above it and it can takes no parameters
 
############################################################################################################


class Book:
    booksNumber = 0
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.booksNumber +=1
        
    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author}, Price: {self.price}"
    
    def getBookPrice(self):
        return f"{self.title} price= {self.price}"
    
    @classmethod
    def getBooksNumbers(cls):
        return f"We have {cls.booksNumber} in the library."
    
    @staticmethod
    def welcomeClass():
        return "Welcome to our library"
    


# Inhertience
class Novel(Book):
    
    def __init__(self,title, author, price):
        super().__init__(title, author, price)
        
    #Override
    def __repr__(self):
        return f"Novel : {self.title}, Author: {self.author}, Price: {self.price}"
    
book1 = Book('Book 1', 'Author 1', 120)
book2 = Book('Book 2', 'Author 2', 220)
book3 = Book('Book 3', 'Author 3', 320)

#print(book1.getBooksNumbers())
print(Book.welcomeClass())

print(book1)
print(book2)
print(book3)

print(book1.getBookPrice())
print(Book.getBooksNumbers())

book3 = Book('Book 4', 'Author 4', 420)
print(Book.getBooksNumbers())

novel1 = Novel('Novel1','author1',200)

print(novel1)

print(Book.getBooksNumbers())
