from typing import Union
import unittest

from sorted_frozen_set import SortedFrozenSet


class TestConstruction(unittest.TestCase):
	def test_contruct_empty(self):
		s = SortedFrozenSet([])
	
	def test_construct_from_non_empty_list(self):
		s = SortedFrozenSet([7, 8, 3, 1])

	def test_construct_from_an_iterator(self):
		items = [7, 8, 3, 1]
		iterator = iter(items)
		s = SortedFrozenSet(iterator)

	def test_construct_no_args(self):
		s = SortedFrozenSet()


class TestContainerProtocol(unittest.TestCase):

	def setUp(self):
		self.s = SortedFrozenSet([6, 7, 3, 9])

	def test_positive_contained(self):
		self.assertTrue(6 in self.s)

	def test_negative_contained(self):
		self.assertFalse(2 in self.s)
	
	def test_positive_not_contained(self):
		self.assertTrue(5 not in self.s)

	def test_negative_not_contained(self):
		self.assertFalse(9 not in self.s)


class TestSizedProtocol(unittest.TestCase):

	#Check for 0 length
	def test_empty_with_default(self):
		s = SortedFrozenSet()
		self.assertEqual(len(s), 0)

	#Check for 0 length
	def test_empty(self):
		s = SortedFrozenSet([])
		self.assertEqual(len(s), 0)

	#Check for length of 1
	def test_one(self):
		s = SortedFrozenSet([42])
		self.assertEqual(len(s), 1)

	#Check for length of 10
	def test_ten(self):
		s = SortedFrozenSet(range(10))
		self.assertEqual(len(s), 10)
	
	#Check that duplicates are not counted in len
	def test_with_duplicates(self):
		s = SortedFrozenSet([5, 5, 5])
		self.assertEqual(len(s), 1)


class TestIterableProtocol(unittest.TestCase):

	def setUp(self):
		self.s = SortedFrozenSet([7, 2, 1, 1, 9])

	def test_iter(self):
		iterator = iter(self.s)
		self.assertEqual(next(iterator), 1)
		self.assertEqual(next(iterator), 2)
		self.assertEqual(next(iterator), 7)
		self.assertEqual(next(iterator), 9)
		self.assertRaises(
			StopIteration,
			lambda: next(iterator)
		)
	
	#This function should work exactly as one above
	def test_for_loop(self):
		expected = [1, 2, 7, 9]
		index = 0
		for item in self.s:
			self.assertEqual(item, expected[index])
			index += 1


if __name__ == "__main__":
	unittest.main()