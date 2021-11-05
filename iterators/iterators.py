# Determine perfect binary tree
def _is_perfect_length(sequence):
	"""True of sequence has length 2n - 1, otherwise False
	"""
	n = len(sequence)
	return ((n + 1) & n == 0) and (n != 0)


class LevelOrderIterator:

	def __init__(self, sequence):
		if not _is_perfect_length(sequence):
			raise ValueError(
				f"Sequence of length {len(sequence)} does not represent "
				"a perfect binary tree with length 2n -1"
			)
		self._sequence = sequence
		self._index = 0

	def __next__(self):
		if self._index >= len(self._sequence):
			raise StopIteration
		result = self._sequence[self._index]
		self._index += 1
		return result

	def __iter__(self):
		return self


# expr_tree = ["*", "+", "-", "a", "b", "c", "d"]


# functions to give index respective of parent
def _left_child(index):
	return 2 * index + 1

def _right_child(index):
	return 2 * index + 2


class PreOrderIterator:
	def __init__(self, sequence):
		if not _is_perfect_length(sequence):
			raise ValueError(
				f"Sequence of length {len(sequence)} does not represent "
				"a perfect binary tree with length 2n -1"
			)
		self._sequence = sequence
		# Start at root node
		self._stack = [0]
	
	def __next__(self):
		# Could test for truthiness, but explicit test 
		# against length better states intent 
		if len(self._stack) == 0:
			raise StopIteration
		
		index = self._stack.pop()
		result = self._sequence[index]

		# Pre-order: Push right child first so left child is 
		# popped and processed first. Last-in, first-out
		right_child_index = _right_child(index)
		if right_child_index < len(self._sequence):
			self._stack.append(right_child_index)

		left_child_index = _left_child(index)
		if left_child_index < len(self._sequence):
			self._stack.append(left_child_index)
		
		return result
	
	def __iter__(self):
		return self


class InOrderIterator:
	def __init__(self, sequence):
		if not _is_perfect_length(sequence):
			raise ValueError(
				f"Sequence of length {len(sequence)} does not represent "
				"a perfect binary tree with length 2n -1"
			)
		self._sequence = sequence
		self._stack = []
		self._index = 0

	def __next__(self):
		if (len(self._stack) == 0) and (self._index >= len(self._sequence)):
			raise StopIteration
		
		# Push left children onto the stack while possible
		while self._index < len(self._sequence):
			self._stack.append(self._index)
			self._index = _left_child(self._index)
		
		# Pop from stack and process, before moving tot he right child
		index = self._stack.pop()
		result = self._sequence[index]
		self._index = _right_child(index)
		return result

	def __iter__(self):
		return self

###################
# IMPERFECT TREES
# Create an empty object (sentinel) to complete
# Can't make a sequence, but you can make a list

# Example: r + p * q

missing = object()
expr_tree = ["+", "r", "*", missing, missing, "p", "q"]

#iterator = InOrderIterator(expr_tree)
#print(" ".join(iterator))	
# # Returns "TypeError: sequence item 0: expected str instance, object found"

# iterator = InOrderIterator(expr_tree)
# print(list(iterator))		
# # Returns [<object object at 0x00000241BD8A84D0>, 'r', <object object at 0x00000241BD8A84D0>, '+', 'p', '*', 'q']
###################


# Make a wrapper for the iterator
class SkipMissingIterator:

	def __init__(self, iterable):
		self._iterator = iter(iterable)

	def __next__(self):
		while True:
			item = next(self._iterator)
			if item is not missing:
				return item
	
	def __iter__(self):
		return self

# Repl Example:
# expr_tree = ["+", "r", "*", missing, missing, "p", "q"]
# iterator = SkipMissingIterator(expr_tree)
# list(iterator)
# Returns ["+", "r", "*", "p", "q"]

# Can also chain (but order is important)
# iterator = SkipMissigIterator(InOrderIterator(expr_trees))
# " ".join(iterator)
# Returns 'r + p * q'