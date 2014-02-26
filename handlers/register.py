#!/usr/bin/env python
# coding=utf-8

from webapp.web import BaseHandler
from model import dbapi


class RegisterHandler(BaseHandler):

    def get(self, error=""):
        params = {'error_info': error}
        body = self.wrap_html('templates/register.html', params)
        self.write(body)

    def post(self):
        email = self.get_arg('email')
        password = self.get_arg('password')
        password2 = self.get_arg('password2')

        user = dbapi.User()
        error = ""
        if email and password == password2:
            if user.get_user(email) == 0:
                error = "user already exist"
            else:
                result = user.insert_user(email, password)
                if result != -1:
                    self.set_secure_cookie('email', str(email))
                    self.redirect("/user")
                else:
                    error = "insert falure, try again later"
        else:
            if password != password2:
                error = "password inconsistent"
            else:
                error = "missing argument"

        self.get(error)
