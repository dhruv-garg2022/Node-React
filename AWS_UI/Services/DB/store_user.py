import sqlite3

def insert(uid,uname,iamid,iamgroup):

    conn = sqlite3.connect('Database/user.db')
    print("Database connected")
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS user ( UserId TEXT,Name TEXT, IAMId TEXT,IAMGroup TEXT, Del TEXT)')
    cur.execute('INSERT INTO user VALUES(?,?,?,?,0)',(uid,uname,iamid,iamgroup))
    # cur.execute("SELECT Access_Key FROM AK")
    # rows=cur.fetchall()
    # print(rows)
    conn.commit()
    conn.close()
# create()