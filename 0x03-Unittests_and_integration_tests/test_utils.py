#!/usr/bin/env python3
"""Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map
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
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
