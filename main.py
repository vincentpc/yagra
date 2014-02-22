#!/usr/bin/env python
# coding=utf-8

from datetime import date
import time

from webapp.web import Application, BaseHandler


URLS = (
    ("/", "Index"),
    ("/hello/(.*)", "Hello"),
)


class Index(BaseHandler):

    def get(self):
        header = "Content-type:text/html\r\n\r\n"
        # self.write(header+"Welcome~")

        body = self.wrap_html('static/index.html')
        self.write(header)
        self.write(body)


class Hello(BaseHandler):

    def get(self, name):

        params = {'name': name, 'date': date.today(), 'time': time.time()}
        header = "Content-type:text/html\r\n\r\n"
        body = self.wrap_html('static/hello.html', params)
        self.write(header)
        self.write(body)

if __name__ == '__main__':
    app = Application(globals(), URLS)
    app.run()
