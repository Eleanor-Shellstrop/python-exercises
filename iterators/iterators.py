# Determine perfect binary tree
def _is_perfect_length(sequence):
	"""True of sequence has length 2n - 1, otherwise False
	"""
	n = len(sequence)
	return ((n + 1) & n == 0) and (n != 0)

# test in repl for length:
# {i: _is_perfect_length(["x"] * i) for i in range(0, 32)}

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