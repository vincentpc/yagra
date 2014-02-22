#!/usr/bin/env python
# coding=utf-8

from webapp.web import Swebapp

URLS = (
    ("/", "Index"),
    ("/hello/(.*)", "Hello"),
)

WSGIAPP = Swebapp(URLS, globals())


class Index:

    def GET(self):
        Swebapp.header('Content-type', 'text/plain')
        return "Welcome~"


class Hello:

    def GET(self, name):
        Swebapp.header('Content-type', 'text/plain')
        return "hello %s\n" % name


if __name__ == '__main__':

    from wsgiref.simple_server import make_server

    httpd = make_server('', 8086, WSGIAPP)
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)

    httpd.serve_forever()
