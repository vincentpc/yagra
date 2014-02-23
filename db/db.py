#!/usr/bin/env python
# coding=utf-8

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="yagra",
                     passwd="abcd!1234",
                     db="yagra",
                     charset="utf8")


def test_insert():
    pass


def test_select():
    import pprint
    sqlstr = "SELECT * FROM yagra_user"
    c = db.cursor()
    c.execute(sqlstr)
    pprint.pprint(c.fetchall())
    c.close()


def dbtest():
    test_insert()
    test_select()
    db.close()


if __name__ == "__main__":
    dbtest()
