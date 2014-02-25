#!/usr/bin/env python
# coding=utf-8

import MySQLdb

import config


db = MySQLdb.connect(host=config.DB_HOST,
                     user=config.DB_USER,
                     passwd=config.DB_PASSWD,
                     db=config.DB_NAME,
                     charset="utf8"
                     )
