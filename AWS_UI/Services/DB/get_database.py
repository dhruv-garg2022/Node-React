import sqlite3

def service():
    con = sqlite3.connect('Database/service_used.db')
    print("Database Connected")
    cur = con.cursor()
    # cur.execute('UPDATE Service_Used SET Del=1, end_date=datetime() WHERE userId=? AND userName=? AND Service=? AND ServiceId=? AND Del="0"',(userid, username, service, serviceid))
    cur.execute('SELECT rowid,* FROM Service_Used')
    rows=cur.fetchall()
    # con.commit()
    con.close()
    return rows
    
def access():
    conn = sqlite3.connect('Database/access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("SELECT rowid,* FROM access_key")
    rows=cur.fetchall()
    # conn.commit()
    conn.close()
    return rows

def user():
    conn = sqlite3.connect('Database/user.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("SELECT rowid,* FROM user")
    rows=cur.fetchall()
    # conn.commit()
    conn.close()
    return rows

# print(service())