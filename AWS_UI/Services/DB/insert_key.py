import sqlite3

def insert(name,a_id):
    conn = sqlite3.connect('Database/access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("INSERT INTO access_key VALUES(?,?,?,'ecom_user','0') ",(name,a_id[0],a_id[1]))
    # rows=cur.fetchall()
    conn.commit()
    conn.close()
    # return rows
    	