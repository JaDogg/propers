# -*- coding: utf-8 -*-


class Property(object):
    def __init__(self, line):
        self.line = line
        key_value = line.split("=", 1)
        self._extract_key(key_value)
        self._extract_value(key_value)

    def _extract_key(self, key_value):
        self.key = key_value[0].strip()
        if not self.key:
            raise PropertyParserException()

    def _extract_value(self, key_value):
        self.value = ""
        if len(key_value) > 1:
            self.value = key_value[1].strip()


class PropertyParserException(Exception):
    pass


class Comment(object):
    def __init__(self, line):
        self.line = line.lstrip()

        if not self.line:
            raise CommentParserException()

        self.data = self.line[self.line.index("#") + 1:]


class CommentParserException(Exception):
    pass
