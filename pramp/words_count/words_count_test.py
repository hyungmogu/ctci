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
        size_expected = len(expected)
        size_result = len(result)

        # verify

        self.assertEqual(size_expected, size_result)
        for item in result:
            self.assertIsNotNone(expected.get(item[0]))
            self.assertEqual(item[1], expected.get(item[0]))

class TestStripPunctuation(unittest.TestCase):

    def setUp(self):
        self.example1 = "hello!"
        self.example2 = "he'd"
        self.example3 = ".hello"

    def test_symbols_are_removed(self):
        # Setup
        expected1 = "hello"
        expected2 = "hed"
        expected3 = "hello"

        # Exercise
        result1 = wc.strip_punctuation(self.example1)
        result2 = wc.strip_punctuation(self.example2)
        result3 = wc.strip_punctuation(self.example3)

        # Verify
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

class TestWordCountEngine(unittest.TestCase):

    def setUp(self):
        self.example = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

    def test_output(self):

        return output

if __name__ == "__main__":
    unittest.main()