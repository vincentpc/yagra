#!/usr/bin/env python
# coding=utf-8

"""application web framework"""

import re


class Swebapp:

    headers = []

    def __init__(self, urls=(), vars={}):
        self._urls = urls
        self._vars = vars

    def __call__(self, environ, start_response):
        self._status = '200 OK'
        del self.headers[:]

        result = self._delegate(environ)
        start_response(self._status, self.headers)

        if isinstance(result, basestring):
            return iter([result])
        else:
            return iter(result)

    def _delegate(self, environ):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        for pattern, name in self._urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                args = m.groups()
                func = method.upper()
                cls = self._vars.get(name)
                if hasattr(cls, func):
                    meth = getattr(cls, func)
                    return meth(cls(), *args)

        return self._notfound()

    def _notfound(self):
        self._status = '404 Not Found'
        self.header('Content-type', 'text/plain')
        return "Not Found\n"

    @classmethod
    def header(cls, name, value):
        cls.headers.append((name, value))
