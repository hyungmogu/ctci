import unittest
import words_count as wc

class TestSortByCount(unittest.TestCase):
    def setUp(self):
        self.example1 = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
        self.example2 = "To be, or not to be,  that is the question:"
        self.example3 = "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "
        self.example4 = "I have failed over and over and over again in my life and that is why I succeed."
        self.example5 = "Look If you had One shot, Or one opportunity, To seize everything you ever wanted, In one moment, Would you capture it, Or just let it slip?"
        self.example6 = "Cause I'm Slim Shady, yes I'm the real Shady, All you other Slim Shadys are just imitating So won't the real Slim Shady, please stand up, Please stand up, Please stand up"

    def test_case_1(self):
        expected = [["just","4"],["practice","3"],["perfect","2"],["makes","1"],["youll","1"],["get","1"],["by","1"]]
        result = wc.word_count_engine(self.example1)
        self.assertEqual(expected, result)

    def test_case_2(self):
        expected = [["to","2"],["be","2"],["or","1"],["not","1"],["that","1"],["is","1"],["the","1"],["question","1"]]
        result = wc.word_count_engine(self.example2)
        self.assertEqual(expected, result)

    def test_case_3(self):
        expected = [["and","4"],["every","3"],["is","3"],["a","3"],["quotation","3"],["all","2"],["book","1"],["house","1"],["out","1"],["of","1"],["forests","1"],["mines","1"],["stone","1"],["quarries","1"],["man","1"],["from","1"],["his","1"],["ancestors","1"]]
        result = wc.word_count_engine(self.example3)
        self.assertEqual(expected, result)

    def test_case_4(self):
        expected = [["over","3"],["and","3"],["i","2"],["have","1"],["failed","1"],["again","1"],["in","1"],["my","1"],["life","1"],["that","1"],["is","1"],["why","1"],["succeed","1"]]
        result = wc.word_count_engine(self.example4)
        self.assertEqual(expected, result)

    def test_case_5(self):
        expected = [["you","3"],["one","3"],["or","2"],["it","2"],["look","1"],["if","1"],["had","1"],["shot","1"],["opportunity","1"],["to","1"],["seize","1"],["everything","1"],["ever","1"],["wanted","1"],["in","1"],["moment","1"],["would","1"],["capture","1"],["just","1"],["let","1"],["slip","1"]]
        result = wc.word_count_engine(self.example5)
        self.assertEqual(expected, result)

    def test_case_6(self):
        expected = [["slim","3"],["shady","3"],["please","3"],["stand","3"],["up","3"],["im","2"],["the","2"],["real","2"],["cause","1"],["yes","1"],["all","1"],["you","1"],["other","1"],["shadys","1"],["are","1"],["just","1"],["imitating","1"],["so","1"],["wont","1"]]
        result = wc.word_count_engine(self.example6)
        self.assertEqual(expected, result)
if __name__ == "__main__":
    unittest.main()