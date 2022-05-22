import sqlite3

def fetch():
    con = sqlite3.connect('Database/service_used.db')
    print("DATABASE CONNECTED")
    cur = con.cursor()
    
    cur.execute("SELECT service_name,Cost FROM Price")
    rows=cur.fetchall()
    
    # cur.execute("DELETE FROM Service_Used WHERE rowid=1 or rowid=2")
    # con.commit()
    con.close()
    return rows
