import sqlite3

def fetch(userid, username):
    con = sqlite3.connect('Database/service_used.db')
    cur = con.cursor()
    cur.execute('SELECT ServiceId FROM Service_Used WHERE userId=? AND userName=? AND Service="s3" AND Del="0"',(userid, username))
    rows=cur.fetchall()
    con.close()
    return rows
