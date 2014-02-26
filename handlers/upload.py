#!/usr/bin/env python
# coding=utf-8

import hashlib
import os
import imghdr
import mimetypes

from webapp.web import BaseHandler
from model import dbapi


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
            #filetype = imghdr.what(fileitem.file)
            # if filetype is None:
            #    self.redirect("user")
            m = hashlib.md5()
            m.update(self.email)
            email_md5 = m.hexdigest()
            open("images/" + email_md5, "wb").write(fileitem.file.read())
            #(x, y, z) = imgfile.getsizes(fileitem.file)
            #thumbnail = imageop.scale(fileitem.file, z, x, y, 64, 64)
            #open("images/" + email_md5+"_small"+filetype, "wb").write(thumbnail.read())
            self.redirect("user")
        else:
            self.redirect("user")
