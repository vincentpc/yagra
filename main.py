#!/usr/bin/env python
# coding=utf-8

from webapp.web import Application


URLS = (
    ("/", "IndexHandler"),
    ("/register?", "RegisterHandler"),
    ("/user", "UserHandler"),
    ("/signin", "SigninHandler"),
    ("/signout", "SignoutHandler"),
    ("/upload", "UploadHandler"),
    ("/avatar/(.*)", "AvatarHandler"),
    ("/error", "ErrorHandler")
)


if __name__ == '__main__':
    app = Application(globals(), URLS)
    app.run()
