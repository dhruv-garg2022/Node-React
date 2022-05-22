import sqlite3

def insert(name,keys):
    conn = sqlite3.connect('access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("INSERT INTO access_key VALUES(?,?,'0')",(name,keys[0]))
    conn.commit()
    conn.close()

def delete(name,keys):
    conn = sqlite3.connect('access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("UPDATE access_key SET Del='1' WHERE Name=? AND Access_Key=? AND Del='0'",(keys[0],name))
    conn.commit()
    conn.close()

insert('dhruv1',['Yo'])
delete('dhruv',['Yo'])