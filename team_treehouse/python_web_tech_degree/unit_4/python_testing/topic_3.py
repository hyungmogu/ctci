# Task 1 of 2
# Our get_anagrams() function raises a ValueError when you pass it an empty string. Finish the test to make sure this happens. You'll want to use assertRaises.

import unittest

from string_fun import get_anagrams

class AnagramTestCase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams('')

# Task 2 of 2
# Now add a new test, test_no_args that should also assertRaises(ValueError). This time, call get_anagrams() with no arguments.

import unittest

from string_fun import get_anagrams

class AnagramTestCase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams('')

    def test_no_args(self):
        with self.assertRaises(ValueError):
            get_anagrams()