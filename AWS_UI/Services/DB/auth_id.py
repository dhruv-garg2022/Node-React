import sqlite3

def create():
    # conn = sqlite3.connect('access_key.db')
    # print("Database connected")
    # cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS access_key (Name TEXT, Access_Key TEXT, Secret_Key TEXT,IAMGroup TEXT, Del TEXT)')
    # # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    # # cur.execute("SELECT Access_Key FROM AK")
    # # rows=cur.fetchall()
    # # print(rows)
    # conn.commit()
    # conn.close()

    conn = sqlite3.connect('../../user.db')
    print("Database connected")
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user ( UserId TEXT,Name TEXT, IAMId TEXT,IAMGroup TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    # cur.execute("SELECT Access_Key FROM AK")
    # rows=cur.fetchall()
    # print(rows)
    conn.commit()
    conn.close()
create()