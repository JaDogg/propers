# -*- coding: utf-8 -*-


class Property(object):
    def __init__(self, line):
        self.line = line
        self.key = line.split("=")[0].strip()
