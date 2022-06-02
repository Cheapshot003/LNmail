import sqlite3

def get_hash(chatid):
    con = sqlite3.connect("../db/payments.db")
    cur = con.cursor()
    daten = cur.execute("SELECT rhash FROM payments WHERE chat_id=\'" + str(chatid) + "\'")
    con.close()
    for i in daten:
        return i[0]

def save_hash(chatid, rhash):
    con = sqlite3.connect("../db/payments.db")
    cur = con.cursor()
    cur.execute("INSERT INTO payments VALUES (\'" + str(chatid) + "\',\'" + str(rhash) + "\')")
    con.commit()
    con.close()
