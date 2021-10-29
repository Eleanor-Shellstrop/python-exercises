class ShippingContainer:

	next_serial = 1337

	@classmethod
	def _generate_serial(cls): # One underscore, implementation detail within the class
		result = cls.next_serial
		cls.next_serial += 1
		return result

	@classmethod
	def create_empty(cls, owner_code, items):
		return cls(owner_code, contents=list(items))

	def __init__(self, owner_code, contents):
		self.owner_code = owner_code 
		self.contents = contents
		self.serial = ShippingContainer._generate_serial()

# Use classmethod when you 
# require access to the class object
# to call other class methods
# or the constructor

# Use staticmethod when you
# don't need access to either
# class or instane objects.
# Most likely an implementation of 
# detail of the class, 
# leading with underscore.
# May be moved globally within module