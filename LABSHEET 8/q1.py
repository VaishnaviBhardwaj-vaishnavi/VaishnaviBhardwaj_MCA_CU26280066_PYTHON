import sqlite3

con = sqlite3.connect("college.db")
print("Database connected successfully!")
con.close()