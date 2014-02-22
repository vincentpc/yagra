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

        body = self.wrap_html('static/index.html')
        self.write(body)


class Hello(BaseHandler):

    def get(self, name):

        params = {'name': name, 'date': date.today(), 'time': time.time()}
        body = self.wrap_html('static/hello.html', params)
        self.write(body)

if __name__ == '__main__':
    app = Application(globals(), URLS)
    app.run()
