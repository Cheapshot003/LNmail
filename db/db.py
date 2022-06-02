import sqlite3

def get_hash(chatid):
    con = sqlite3.connect("payments.db")
    cur = con.cursor()
    daten = cur.execute("SELECT rhash FROM payments WHERE chat_id=\'" + str(chatid) + "\'")
    
    for i in daten:
        soos = i[0]
    con.close()
    return soos

def save_hash(chatid, rhash):
    con = sqlite3.connect("payments.db")
    cur = con.cursor()
    cur.execute("INSERT INTO payments VALUES (\'" + str(chatid) + "\',\'" + str(rhash) + "\')")
    con.commit()
    con.close()
