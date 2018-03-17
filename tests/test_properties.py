# -*- coding: utf-8 -*-
import unittest

from propers.properties import Property


class PropertiesTestCase(unittest.TestCase):
    def test_property_creation(self):
        prop = Property("a=b")
        self.assertTrue(prop is not None)

    def test_key_split(self):
        tests = (
            ("a=b", "a"),
            ("x = y", "x")
        )
        for line, expected in tests:
            prop = Property(line)
            self.assertEqual(
                prop.key, expected,
                "{0}|prop.key={1}"
                    .format(repr(line), repr(expected)))
