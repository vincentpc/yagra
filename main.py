#!/usr/bin/env python
# coding=utf-8

from datetime import date
import time
import hashlib
import os

from webapp.web import Application, BaseHandler
from model import dbapi


URLS = (
    ("/", "IndexHandler"),
    ("/hello/(.*)", "Hello"),
    ("/register?", "RegisterHandler"),
    ("/user", "UserHandler"),
    ("/signin", "SigninHandler"),
    ("/signout", "SignoutHandler"),
    ("/upload", "UploadHandler")
)

class UploadHandler(BaseHandler):
    def check(self):
        email = self.get_secure_cookie("email")
        user = dbapi.User()
        if email and user.get_user(email) == 0:
            profile = user.get_user_all(email)
            if profile:
                self.id = profile[0]
                self.time = profile[4]
                self.email = email
        else:
            self.clear_cookies()
            self.redirect("/")

    def post(self):
        self.check()
        fileitem = self.request.files["filename"]
        if fileitem.filename:
            #fn = os.path.basename(fileitem.filename)
            m = hashlib.md5()
            m.update(self.email)
            email_md5 = m.hexdigest()
            open("images/" + email_md5, "wb").write(fileitem.file.read())
            self.redirect("user")
        else:
            self.redirect("user")


class SignoutHandler(BaseHandler):

    def get(self):
        self.clear_cookies()
        self.redirect("/")

    def post(self):
        self.get()

class UserHandler(BaseHandler):

    def check(self):
        email = self.get_secure_cookie("email")
        user = dbapi.User()
        if email and user.get_user(email) == 0:
            profile = user.get_user_all(email)
            if profile:
                self.time = profile[4]
                self.email = email
        else:
            self.clear_cookies()
            self.redirect("/")

    def get(self):
        self.check()
        m = hashlib.md5()
        m.update(self.email)
        email_md5 = m.hexdigest()
        fn = "images/" + email_md5
        if os.path.isfile(fn):
            imagetag =  """<img src="%s" class="rounded" alt="Upload Image Below">""" % fn
        else:
            imagetag = """<p>Avatar Not Available. Upload One!</p>"""
        params = {'name': self.email, 'time': self.time, 'image': imagetag}
        body = self.wrap_html('templates/user.html', params)
        self.write(body)


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


class RegisterHandler(BaseHandler):

    def get(self, error=""):
        params = {'error_info': error}
        body = self.wrap_html('templates/register.html', params)
        self.write(body)

    def post(self):
        email = self.get_arg('email')
        password = self.get_arg('password')

        user = dbapi.User()
        error = ""
        if email:
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
            error = "missing argument"

        self.get(error)


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


class Hello(BaseHandler):

    def get(self, name):

        params = {'name': name, 'date': date.today(), 'time': time.time()}
        body = self.wrap_html('static/hello.html', params)
        self.write(body)

if __name__ == '__main__':
    app = Application(globals(), URLS)
    app.run()
