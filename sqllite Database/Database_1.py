
import sqlite3

def readingDB(fileName):
    
    try:
        
        #connecting to database
        dbObject = sqlite3.connect(fileName)
        
        #printing message that database is connected successfully
        print("DataBase connected Successfully\n")
        
        #making cursur
        cr = dbObject.cursor()
        
        #selecting the table
        cr.execute("SELECT * FROM users")
        
        #fetching data from database    
        results = cr.fetchall()
        
        print(f"the table has = {len(results)} = ROWS")
        
        for row in results:
            print(f"UserName ==> {row[0]}",end="  ")
            print(f"UserID ==> {row[1]}")
            
        print("")
            
    except sqlite3.Error:

        #printing Error message
        print(f"Error in reading data ==> {sqlite3.Error}")
    
    finally:
        if(dbObject):
            
            #closing the database after finishing
            dbObject.close()
            
            #printing message that database closed successfully
            print("database closed...")
            

#calling the readingDB function

readingDB("app.db")