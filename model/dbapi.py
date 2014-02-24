#!/usr/bin/env python
# coding=utf-8

import time
import hashlib
import globaldb


class User(object):

    def __init__(self):
        self.db = globaldb.db

    # password encoding
    def encode_pwd(self, str):
        if str is not None:
            m = hashlib.md5()
            m.update(str)
            return m.hexdigest()
        else:
            return ""

    def insert_user(self, email, password):
        password = self.encode_pwd(password)
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
        c = self.db.cursor()
        try:
            c.execute(sqlstr, (email, password, email,
                               time.strftime('%Y-%m-%d %H:%M:%S')))
            self.db.commit()
            lastinsertid = c.lastrowid
            return lastinsertid
        except:
            self.db.rollback()
            return -1

    def get_user(self, name):
        sqlstr = "SELECT * FROM yagra_user WHERE user_email = %s"
        c = self.db.cursor()
        c.execute(sqlstr, (name))
        result = c.fetchall()

        if len(result) is not 0:
            return 0
        else:
            return -1


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
    import sys
    test_insert(sys.argv[1])
    test_select()
    globaldb.db.close()


if __name__ == "__main__":
    dbtest()
