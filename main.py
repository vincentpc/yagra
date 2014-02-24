#!/usr/bin/env python
# coding=utf-8

from datetime import date
import time

from webapp.web import Application, BaseHandler
from model import dbapi


URLS = (
    ("/", "IndexHandler"),
    ("/hello/(.*)", "Hello"),
    ("/register?", "RegisterHandler"),
    ("/user", "UserHandler")
)

class UserHandler(BaseHandler):
    def check(self):
       
        self.email = "test"

    def get(self):
        self.check()
        params = {'name': self.email}
        body = self.wrap_html('templates/user.html', params)
        self.write(body)


class RegisterHandler(BaseHandler):

    def get(self, error=""):
        params = {'error_info': error}
        body = self.wrap_html('templates/register.html', params)
        self.write(body)

    def post(self):
        email = self.get_arg('email')
        password = self.get_arg('password')

        user = dbapi.User()
        if email:
            if user.get_user(email) == -1:
                error = "user already exist"

            result = user.insert_user(email, password)
            if result != -1:
                self.redirect("/user")
            else:
                error = "insert falure, try again later"
        else:
            error = "missing argument"

        self.get(error)


class IndexHandler(BaseHandler):

    def get(self):

        body = self.wrap_html('templates/index.html')
        self.write(body)


class Hello(BaseHandler):

    def get(self, name):

        params = {'name': name, 'date': date.today(), 'time': time.time()}
        body = self.wrap_html('static/hello.html', params)
        self.write(body)

if __name__ == '__main__':
    app = Application(globals(), URLS)
    app.run()
