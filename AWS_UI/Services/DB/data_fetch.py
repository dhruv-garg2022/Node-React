import sqlite3

def fetch(name):
    conn = sqlite3.connect('Database/access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("SELECT Access_Key,Secret_Key FROM access_key WHERE Name=? AND Del='0'",(name,))
    rows=cur.fetchall()
    conn.close()
    return rows