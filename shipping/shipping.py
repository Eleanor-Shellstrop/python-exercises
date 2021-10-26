class ShippingContainer:

	next_serial = 1337

	def __init__(self, owner_code, contents):
		self.owner_code = owner_code # Instance attributes (self)
		self.contents = contents
		self.serial = ShippingContainer.next_serial # Class attributes
		ShippingContainer.next_serial += 1
		
#  If we attempted to assign to an existing class attribute 
# through the self reference, we would actually 
# create a new instance attribute, 
# which would hide the class attribute, 
# and the class attribute would remain unmodified.