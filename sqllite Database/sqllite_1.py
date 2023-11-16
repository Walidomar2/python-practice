
import sqlite3

# connect to database if it's exists or creating it 
db = sqlite3.connect("app.db")

# execute the query you want
#db.execute("CREATE TABLE if not exists skills (name text, progress integer, userID integer)")

# you should with cursor better

cr = db.cursor()

cr.execute("CREATE TABLE if not exists users (name text, userID integer)")
cr.execute("CREATE TABLE if not exists skills (skill text, progress integer, userID integer)")

usersList = ['Walid', 'Omar', 'Karem', 'Osama', 'Ahmed', 'Mohamed']

for id,name in enumerate(usersList):
    cr.execute(f"INSERT INTO users(name, userID) VALUES ('{name}', {id + 1})")

#cr.execute("SELECT name FROM users")
#cr.execute("SELECT name,userID FROM users")
cr.execute("SELECT * from users")

#print(cr.fetchone())   ==> just one row
#print(cr.fetchmany(2)) ==> 2 rows
print(cr.fetchall())   #==> list of tuples has all rows


# you must save changes first (commit)
db.commit()
# close the database
db.close()




