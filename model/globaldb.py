#!/usr/bin/env python
# coding=utf-8

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="yagra",
                     passwd="abcd!1234",
                     db="yagra",
                     charset="utf8"
                    )
