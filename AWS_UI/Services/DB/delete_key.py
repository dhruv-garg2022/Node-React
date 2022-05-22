import sqlite3

def delete(name,a_id):
    conn = sqlite3.connect('Database/access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("DELETE FROM access_key WHERE Name=? AND Access_Key=? AND Del='0'",(name, a_id))
    # rows=cur.fetchall()
    conn.commit()
    conn.close()
    # return rows
