import unittest
from unittest.mock import patch
from io import StringIO
import ccwc


class TestFileCounter(unittest.TestCase):

    def test_count_bytes(self):
        input_string = "Hello, world!"
        result = ccwc.count_bytes(input_string)
        self.assertEqual(result, len(input_string))

    def test_count_lines(self):
        content = "Line 1\nLine 2\nLine 3"
        with patch('builtins.open', return_value=StringIO(content)):
            result = ccwc.count_lines('mocked_file.txt')
        self.assertEqual(result, 3)

    def test_count_words(self):
        content = "This is a sample sentence."
        with patch('builtins.open', return_value=StringIO(content)):
            result = ccwc.count_words('mocked_file.txt')
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
