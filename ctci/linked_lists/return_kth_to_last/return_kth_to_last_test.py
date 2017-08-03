import unittest
import return_kth_to_last as r


class TestKthToLastMethod(unittest.TestCase):

	def test_when_head_is_null(self):
		li = r.LinkedList()

		self.assertEqual(li.get_kth_to_last_element(3), None)

	def test_when_there_is_only_one_node(self):
		e1 = r.Element(1)
		li = r.LinkedList(e1)

		element = li.get_kth_to_last_element(3)

		self.assertEqual(element.value, 1)

	def test_when_there_is_more_than_one_node(self):
		e1 = r.Element(1)
		e2 = r.Element(2)
		e3 = r.Element(3)
		e4 = r.Element(4)

		li = r.LinkedList(e1)
		li.append(e2)
		li.append(e3)
		li.append(e4)

		element = li.get_kth_to_last_element(2)

		self.assertEqual(element.value, 2)


if __name__ == "__main__":
	unittest.main()