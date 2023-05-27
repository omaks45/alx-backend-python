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
    """_summary_
    Args:
        unittest(_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Args:
            url: url to send http request
            plaload: expected json response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """_summary_

    Args:
                    unittest (_type_): _description_
    """

    def test_memoize(self):
        """_summary_

        Returns:
                _type_: _description_
        """

        class TestClass:
            """_summary_
            """

            def a_method(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
