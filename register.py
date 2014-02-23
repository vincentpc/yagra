#!/usr/bin/env python
# coding=utf-8

from webapp.web import BaseHandler
from db import db

class RegisterHandler(BaseHandler):
    def get(self):
       body = self.wrap_html('static/register.html')
       self.write(body)

    def post(self):
        pass
