# coding:utf-8
# __autor__:'cyb'
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect("testsqlite.db")
con.row_factory = dict_factory
cur = con.cursor()
cur.execute("select * from employee ")
print(cur.fetchone())




def dict_factory(cursor, row):
    return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))
