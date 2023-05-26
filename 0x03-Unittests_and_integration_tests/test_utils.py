#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to
test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to
test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual
that the function returns the expected result.

The body of the test method should not be longer than 2 lines.
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a"), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        summary
        """
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        summary
        """
        with self.assertRaises(expected) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, url, expected):
        """
        summary
        """
        mock_res = Mock()
        mock_res.json.return_value = expected
        with patch("request.get", return_value=mock_res):
            response = get_json(url)

            self.assertEqual(response, expected)
