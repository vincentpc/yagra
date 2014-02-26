#!/usr/bin/env python
# coding=utf-8

from webapp.web import BaseHandler
from model import dbapi


class IndexHandler(BaseHandler):

    def get(self):

        email = self.get_secure_cookie("email")
        user = dbapi.User()
        if email and user.get_user(email) == 0:
            self.redirect("/user")
        else:
            self.clear_cookies()
            body = self.wrap_html('templates/index.html')
            self.write(body)
