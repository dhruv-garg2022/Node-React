import sqlite3

def generate(userid, username):
    con = sqlite3.connect('Database/service_used.db')
    print("DATABASE CONNECTED")
    cur = con.cursor()
    
    cur.execute("SELECT ServiceId, Service, JULIANDAY(end_date) - JULIANDAY(create_date),end_date FROM Service_Used WHERE userId=? AND userName=? AND PAID=0 AND Del=1",(userid, username))
    rows=cur.fetchall()
    cur.execute("SELECT ServiceId, Service, JULIANDAY(datetime()) - JULIANDAY(create_date),datetime() FROM Service_Used WHERE userId=? AND userName=? AND PAID=0 AND Del=0",(userid, username))
    new_rows=cur.fetchall()
    rows+=new_rows
    # print(rows)
    # cur.execute("DELETE FROM Service_Used WHERE rowid=1 or rowid=2")
    # con.commit()
    con.close()
    return rows
# generate('1','dhruv')