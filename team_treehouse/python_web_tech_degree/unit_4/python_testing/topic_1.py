# ============= Part 1 =============
# Task 1 of 1
# Add a doctest to average() that tests the function with the list [1, 2]. Because of how we test doctests, you'll need to leave a blank line at the end of your doctest before the closing quotes.

def average(num_list):
    """Return the average for a list of numbers

    >>> average([1,2])
    1.5

    """
    return sum(num_list) / len(num_list)


# ============= Part 2 =============
# Task 1 of 2
# Import the unittest module.

import unittest

# Task 2 of 2
# Create a TestCase named SimpleTestCase with a simple test that asserts that 10 - 10 is 0. Remember, unittest test names have to start with test_.