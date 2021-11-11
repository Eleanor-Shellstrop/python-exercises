import math


class InclinationError(Exception):
	pass


def inclination(dx, dy):
	try:
		return math.degrees(math.atan(dy / dx))
	except ZeroDivisionError as e:
		raise InclinationError("Slope cannot be vertical") from e

# Explicit Exeception Chaining:
# except <original exception type> as e:
# raise <new exception type> from e