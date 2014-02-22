#!/usr/bin/env python
# coding=utf-8

import os
import cgi
import Cookie
import re
import sys

default_headers = {"Content-type": "text/plain"}


class Httprequest(object):

    def __init__(self, meth, uri, query_str, host, headers, cookies=""):
        self.meth = meth
        self.uri = uri
        self.cookies_str = cookies
        self.host = host
        self.headers = headers

        self.path = uri.split("?", 1)[0]
        self.args = {}
        self.files = {}

        form = cgi.FieldStorage()
        for key in form.keys():
            item = form[key]
            if item.file:
                self.files[key] = item

            self.args[key] = form.getlist(key)

    def write(self, text):
        sys.stdout.write(text)

    @property
    def set_cookies(self):
        if not hasattr(self, "_cookies"):
            self._cookies = Cookie.SerialCookie()
            if self.cookies_str:
                self._cookies.load(self.cookies_str)
        return self._cookies


class TemplateWrapper(object):
    def __init__(self):
        pass

    @staticmethod
    def wrap_html(path, params):
        body = open(path, 'r').read()
        if params:
            body = body % params
        return body

class BaseHandler(object):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__()
        self.app = application
        self.request = request

        self.clear()

    def clear(self):
        self._status_code = 200

    def write(self, text):
        self.request.write(text)

    def wrap_html(self, path, params=None):
        return TemplateWrapper.wrap_html(path, params)


class Application(object):

    """web framework for the application"""

    def __init__(self, vars, urls=(), config=()):
        self._urls = urls
        self._config = config
        self._vars = vars

    def get_request(self):
        env = os.environ

        headers = default_headers

        request = Httprequest(
            unicode(env["REQUEST_METHOD"], encoding="utf-8"),
            unicode(env["REQUEST_URI"], encoding="utf-8"),
            unicode(env.get("QUERY_STRING"), encoding="utf-8"),
            unicode(env.get("HTTP_HOST"), encoding="utf-8"),
            headers,
            env.get("HTTP_COOKIE")

        )

        return request

    def delegate(self):
        path = self._request.path
        method = self._request.meth

        for pattern, name in self._urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                args = m.groups()
                func = method.lower()
                cls = self._vars.get(name)

                if hasattr(cls, func):
                    handler = cls(self, self._request)
                    meth = getattr(cls, func)
                    return meth(handler, *args)

        return self._notfound()

    def _notfound(self):
        self._status = '404 Not Found'

    def handle(self):
        self._request = self.get_request()
        self.delegate()

    def run(self):
        self.handle()
