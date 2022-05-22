import sqlite3

def delete(userid, username, service, serviceid):
    con = sqlite3.connect('Database/service_used.db')
    cur = con.cursor()
    cur.execute('UPDATE Service_Used SET Del=1, end_date=datetime() WHERE userId=? AND userName=? AND Service=? AND ServiceId=? AND Del="0"',(userid, username, service, serviceid))
    # cur.execute('DELETE FROM Service_Used')
    con.commit()
    con.close()
    
