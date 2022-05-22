import sqlite3

def delete(services, userid, username):
    con = sqlite3.connect('Database/service_used.db')
    print("DATABASE CONNECTED")
    cur = con.cursor()
    
    for data in services:
        print("\n\n\ndata",data,"\n\n\n")
        cur.execute("UPDATE Service_Used SET PAID=1 WHERE userId=? AND userName=? AND ServiceId=? AND Service=? AND Del=1",( userid, username,data[0],data[1]))
        cur.execute("UPDATE Service_Used SET PAID=0, create_date=? WHERE userId=? AND userName=? AND ServiceId=? AND Service=? AND Del=0",( data[3], userid, username,data[0],data[1]))
    # cur.execute("SELECT ServiceId, Service, JULIANDAY(end_date) - JULIANDAY(create_date) FROM Service_Used WHERE userId=? AND userName=? AND PAID=0",(userid, username))
    # rows=cur.fetchall()
    # print(rows)
    # cur.execute("DELETE FROM Service_Used WHERE rowid=1 or rowid=2")
    con.commit()
    con.close()
    # return rows
# generate('1','dhruv')