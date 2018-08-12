import unittest
import words_count as wc

class TestSortByCount(unittest.TestCase):
    def setUp(self):
        self.example = [["hi", 2], ["yolo", 1], ["hello", 3]]

    def test_output(self):
        # setup
        sample_size = len(self.example)
        expected = [["hello", 3], ["hi", 2], ["yolo", 1]]

        #exercise
        wc.sort_by_count(self.example)

        # verify
        for index in range(sample_size):
            self.assertEqual(self.example[index][0], expected[index][0])
            self.assertEqual(self.example[index][1], expected[index][1])


class TestCountKeyWords(unittest.TestCase):

    def setUp(self):
        self.example = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

    def test_size_of_expected_and_result_must_equal(self):
        # setup
        expected = 8

        # exercise
        result = len(wc.count_keywords(self.example))

        # verify
        self.assertEqual(result, expected)

    def test_output(self):
        # setup
        expected = {
            "practice": "3",
            "makes": "1",
            "perfect": "2",
            "youll": "1",
            "only": "1",
            "get": "1",
            "by": "1",
            "just": "1"
        }

        # exercise
        result = wc.count_keywords(self.example)

        # verify
        for item in result:
            self.assertIsNotNone(expected.get(item[0]))
            self.assertEqual(item[1], expected.get(item[0]))

class TestStripPunctuation(unittest.TestCase):

    def setUp(self):
        self.example1 = "hello!"
        self.example2 = "he'd"
        self.example3 = ".hello"

    def test_symbols_in_beginning_is_removed(self):
        expected = "hello"

        result = wc.strip_punctuation(self.example3)

        self.assertEqual(result, expected)

    def test_symbols_in_mid_is_removed(self):
        expected = "hed"

        result = wc.strip_punctuation(self.example2)

        self.assertEqual(result, expected)

    def test_symbols_at_end_is_removed(self):
        # Setup
        expected = "hello"

        # Exercise
        result = wc.strip_punctuation(self.example1)

        # Verify
        self.assertEqual(result, expected)

class TestWordCountEngine(unittest.TestCase):

    def setUp(self):
        self.example = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

    def test_size_of_expected_and_result_must_equal(self):
        expected  = 8

        result = len(wc.words_count_engine(self.example))

        self.assertEqual(expected, result)

    def test_count_is_in_decreasing_order(self):
        expected  = ["3","2","1","1","1","1","1","1"]

        # exercise
        result = wc.words_count_engine(self.example)

        for index in range(len(result)):
            self.assertEqual(result[index][1], expected[index])


if __name__ == "__main__":
    unittest.main()