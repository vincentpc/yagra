#!/usr/bin/env python
# coding=utf-8

from webapp.web import BaseHandler
from model import dbapi


class SigninHandler(BaseHandler):

    def post(self):
        email = self.get_arg("email")
        password = self.get_arg("password")
        if email:
            user = dbapi.User()
            if user.check_user(email, password) == 0:
                self.set_secure_cookie('email', str(email))
                self.redirect("/user")

        self.redirect("/")
