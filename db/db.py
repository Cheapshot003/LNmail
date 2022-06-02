import sqlite3

def get_hash(chatid):
    con = sqlite3.connect("../db/payments.db")
    cur = con.cursor()
    daten = cur.execute("SELECT rhash FROM payments WHERE chat_id=\'" + str(chatid) + "\'")
    print(daten(0)[0])

get_hash(34534524)
