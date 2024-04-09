#!/usr/bin/env python3
"""Test for utils.py

This module contains a unit test for the `access_nested_map` function.
The `TestAccessNestedMap` class defines the unit test cases
using the `parameterized` decorator.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map

    This class defines the unit test cases for the
    `access_nested_map` function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, error):
        """Test access_nested_map exception

        This method tests the `access_nested_map` function by passing different
        inputs that should raise an exception.
        """
        with self.assertRaises(error):
            self.assertEqual(access_nested_map(nested_map, path))


if __name__ == "__main__":
    unittest.main()
