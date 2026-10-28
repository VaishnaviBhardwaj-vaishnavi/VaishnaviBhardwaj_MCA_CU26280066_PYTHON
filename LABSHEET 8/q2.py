import sqlite3

con = sqlite3.connect("newcollege.db")
print("Database created successfully!")
con.close()