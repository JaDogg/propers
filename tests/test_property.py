# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized

from propers.properties import Property, PropertyParserException


class CommentTestCase(unittest.TestCase):
    def test_property_creation(self):
        prop = Property("a=b")
        self.assertTrue(prop is not None)

    @parameterized.expand([
        ("a=b", "a", "b"),
        ("x = y", "x", "y"),
        ("product.version = 1.2.3", "product.version", "1.2.3"),
        ("some=key", "some", "key"),
        ("no.value=", "no.value", ""),
        ("no.value", "no.value", ""),
        ("v==1", "v", "=1"),
        ("v=#1", "v", "#1"),
        ("v#=#1", "v#", "#1"),
        ("v#==#1", "v#", "=#1")
    ])
    def test_property_split(self, line, key, value):
        prop = Property(line)
        message = "input={0}|prop.key={1}|" \
                  "prop.value={2}".format(repr(line), key, value)
        self.assertEqual(prop.key, key, message)
        self.assertEqual(prop.value, value, message)

    @parameterized.expand([
        ("=b",),
        ("",)
    ])
    def test_property_split_errors(self, line):
        with self.assertRaises(PropertyParserException):
            _ = Property(line)
