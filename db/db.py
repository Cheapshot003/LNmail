import sqlite3

def get_hash(chatid):
    con = sqlite3.connect("../db/payments.db")
    cur = con.cursor()
    daten = cur.execute("SELECT rhash FROM payments WHERE chat_id=\'" + str(chatid) + "\'")
    for i in daten:
        print(i[0])

get_hash(34534524)
