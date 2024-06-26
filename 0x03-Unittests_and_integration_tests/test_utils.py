#!/usr/bin/env python3
"""Test for utils.py

This module contains a unit test for the `access_nested_map` function.
The `TestAccessNestedMap` class defines the unit test cases
using the `parameterized` decorator.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """Test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get) -> None:
        """Test get_json"""
        mock_json = Mock()
        mock_json.json.return_value = test_payload
        mock_get.return_value = mock_json

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class for Testing Memoize"""

    def test_memoize(self):
        """
        Test memoize method tests the functionality of the `memoize` decorator.
        It creates a `TestClass` instance and checks if the `a_property`
        method is memoized correctly by mocking the `a_method` method.
        """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_a_method:
            mock_a_method.return_value = 10

            instance_of_test_class = TestClass()
            res = instance_of_test_class.a_property
            self.assertEqual(instance_of_test_class.a_property, res)
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
