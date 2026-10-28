import sqlite3

try:
    con = sqlite3.connect("college.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM unknown_table")
    print(cur.fetchall())

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "con" in locals():
        con.close()