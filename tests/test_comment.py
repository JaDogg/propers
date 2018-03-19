# -*- coding: utf-8 -*-
import unittest

from parameterized import parameterized

from propers.properties import Comment, CommentParserException


class PropertyTestCase(unittest.TestCase):
    @parameterized.expand([
        ("# Some comment", " Some comment"),
        ("  # Some comment", " Some comment"),
        ("#### Some comment", "### Some comment"),
        (" #### Some comment ", "### Some comment "),
    ])
    def test_parse_comment(self, line, data):
        comment = Comment(line)
        self.assertEqual(comment.data, data)

    @parameterized.expand([
        ("          ",),
        ("",)
    ])
    def test_parse_comment_errors(self, line):
        with self.assertRaises(CommentParserException):
            _ = Comment(line)
