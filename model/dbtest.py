#!/usr/bin/env python
# coding=utf-8

import globaldb
import time

def test_insert(name="vincent"):
    sqlstr = """
        INSERT INTO `yagra`.`yagra_user`
        (
        `user_login`,
        `user_passwd`,
        `user_email`,
        `user_time`
        )
        VALUES
        (%s, %s, %s, %s)
    """
    c = globaldb.db.cursor()
    c.execute(sqlstr, (name, "1234", name + "@gmail.com",
                       time.strftime('%Y-%m-%d %H:%M:%S')))
    globaldb.db.commit()


def test_select():
    import pprint
    sqlstr = "SELECT * FROM yagra_user"
    c = globaldb.db.cursor()
    c.execute(sqlstr)
    pprint.pprint(c.fetchall())
    c.close()


def dbtest():
    #import sys
    #test_insert(sys.argv[1])
    test_select()
    globaldb.db.close()


if __name__ == "__main__":
    dbtest()
