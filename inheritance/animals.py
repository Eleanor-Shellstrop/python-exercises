class Animal:
	@classmethod
	def description(cls):
		return "An Animal"


# using super() with classmethod
class Bird(Animal):
	@classmethod
	def description(cls):
		# See how it works:
		# s = super()
		# print(s) //Returns <super: <class 'Bird'>, <Flamingo object>>
		return super().description() + " with wings"


class Flamingo(Bird):
	@classmethod
	def description(cls):
		return super().description() + " and fabulous pink feathers"


# call in repl
# Animal.description()
# Bird.description()
# Flamingo.description()