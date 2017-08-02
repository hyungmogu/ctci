import unittest
import palindrome as p

class TestGetNode(unittest.TestCase):

	def test_when_head_is_empty(self):
		li = p.LinkedList()
		self.assertEqual(li.get_node(10), None)

	def test_when_there_is_one_node(self):
		e1 = p.Element(1)
		li = p.LinkedList(e1)
		self.assertEqual(li.get_node(0), e1)

	def test_when_there_are_more_nodes(self):

		e1 = p.Element(1)
		e2 = p.Element(2)
		e3 = p.Element(3)
		e4 = p.Element(4)

		li = p.LinkedList(e1)
		li.append(e2)
		li.append(e3)
		li.append(e4)

		self.assertEqual(li.get_node(1), e2)


class TestGetSize(unittest.TestCase):

	def setUp(self):

		e1 = p.Element(1)
		e2 = p.Element(2)
		e3 = p.Element(3)
		e4 = p.Element(4)

		self.li = p.LinkedList(e1)
		self.li.append(e2)
		self.li.append(e3)
		self.li.append(e4)

	def test_when_head_is_not_empty(self):
		self.assertEqual(self.li.get_size(), 4)

	def test_when_head_is_empty(self):	

		li2 = p.LinkedList()

		self.assertEqual(li2.get_size(), 0)


class TestIsPalindrome(unittest.TestCase):

	def test_when_head_is_empty(self):
		li = p.LinkedList()		
		self.assertEqual(li.is_palindrome(), False)


	def test_when_there_is_one_node(self):
		e1 = p.Element(1)
		li = p.LinkedList(e1)
		self.assertEqual(li.is_palindrome(), True)


	def test_when_there_are_more_than_one_node(self):
		e1 = p.Element(1)
		e2 = p.Element(2)
		e3 = p.Element(2)
		e4 = p.Element(1)
		e5 = p.Element(4)

		li = p.LinkedList(e1)
		li.append(e2)
		li.append(e3)
		li.append(e4)		

		self.assertEqual(li.is_palindrome(), True)

		li.append(e5)

		self.assertEqual(li.is_palindrome(), False)

if __name__ == "__main__":
	unittest.main()