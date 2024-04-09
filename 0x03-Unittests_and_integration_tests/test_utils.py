#!/usr/bin/env python3
"""Test for utils.py

This module contains a unit test for the `access_nested_map` function.
The `TestAccessNestedMap` class defines the unit test cases using the `parameterized` decorator.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map

    This class defines the unit test cases for the `access_nested_map` function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self,
                               nested_map: Dict[str, Any],
                               path: Tuple[str, ...],
                               expected: Any) -> None:
        """Test access_nested_map

        This method tests the `access_nested_map` function by passing different inputs
        and asserting that the returned value matches the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
