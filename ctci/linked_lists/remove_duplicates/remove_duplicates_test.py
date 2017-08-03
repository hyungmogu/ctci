import unittest
import remove_duplicates as r


class TestRemoveDuplicateMethod(unittest.TestCase):
	def test_when_head_is_null(self):
		li = r.LinkedList()
		self.assertEqual(li.is_empty(), True)

	def test_when_only_one_node_exists(self):
		e1 = r.Element(1)

		li = r.LinkedList(e1)
		li.remove_duplicates()
		self.assertEqual(li.display(), "1")

	def test_when_there_are_duplicates_in_the_array(self):
		e1 = r.Element(1)
		e2 = r.Element(1)
		e3 = r.Element(2)
		e4 = r.Element(2)
		e5 = r.Element(3)

		li = r.LinkedList(e1)
		li.append(e2)
		li.append(e3)
		li.append(e4)
		li.append(e5)

		li.remove_duplicates()
		self.assertEqual(li.display(), "1 2 3")

	def test_when_there_are_no_duplicates_in_the_array(self):
		e1 = r.Element(1)
		e2 = r.Element(2)
		e3 = r.Element(3)

		li = r.LinkedList(e1)

if __name__ == "__main__":
	unittest.main()

