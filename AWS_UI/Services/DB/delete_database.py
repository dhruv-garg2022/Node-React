import sqlite3

def delete1():
    con = sqlite3.connect('../../Database/service_used.db')
    cur = con.cursor()
    # cur.execute('UPDATE Service_Used SET Del=1, end_date=datetime() WHERE userId=? AND userName=? AND Service=? AND ServiceId=? AND Del="0"',(userid, username, service, serviceid))
    cur.execute('DELETE FROM Service_Used')
    con.commit()
    con.close()
    
def delete2():
    conn = sqlite3.connect('../../Database/access_key.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("DELETE FROM access_key")
    # rows=cur.fetchall()
    conn.commit()
    conn.close()

def delete3():
    conn = sqlite3.connect('../../Database/user.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS AK (Name TEXT, Access_Key TEXT, Del TEXT)')
    # cur.execute('INSERT INTO AK VALUES("Dhruv","123","1")')
    cur.execute("DELETE FROM user")
    # rows=cur.fetchall()
    conn.commit()
    conn.close()

delete1()
delete2()
delete3()