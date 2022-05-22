import sqlite3

def insert(userid, username, service, serviceid):
    con = sqlite3.connect('Database/service_used.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Service_Used VALUES(?,?,?,?,0,datetime(),datetime(),0)',(userid, username, service, serviceid))
    con.commit()
    con.close()