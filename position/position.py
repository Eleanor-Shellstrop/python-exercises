class Position:

	def __init__(self, latitude, longitude):
		if not(-90 <= latitude <= +90):
			raise ValueError(f"Latitude {latitude} out of range")

		if not (-180 <= longitude <= +180):
			raise ValueError(f"Longitude {longitude} is out of range")
		
		self._latitude = latitude
		self._longitude = longitude
	
	@property
	def latitude(self):
		return self._latitude
	
	@property
	def longitude(self):
		return self._longitude

	@property
	def latitude_hemisphere(self):
		return "N" if self.latitude >= 0 else "S"
	
	@property
	def longitude_hemisphere(self):
		return "E" if self.longitude >= 0 else "W"

	# For new representation
	def __repr__(self):
		# Also acceptable: return f"{self.__class__.__name__} ...
		return f"{typename(self)} (latitude={self.latitude}, longitude={self.longitude})"

	def __str__(self):
		return format(self)

	def __format__(self, format_spec):
		component_format_spec = ".2f"
		# Check for float:
		prefix, dot, suffix = format_spec.partition(".")
		if dot:
			num_decimal_places = int(suffix)
			component_format_spec = f".{num_decimal_places}f"
			# Example of this working:
			# matterhorn = EarthPosition(45.9763, 7.586)
			# format(matterhorn, ".1") // Returns (46.0 N, 7.7 E)
		latitude = format(abs(self.latitude), component_format_spec)
		longitude = format(abs(self.longitude), component_format_spec)
		return (
			f"{latitude}° {self.latitude_hemisphere}, "
			f"{longitude}° {self.longitude_hemisphere}"
		)
		

# __format__ can specify floats:
# '7.748091e-05'
# format(q, "f") returns '0.000077'
# format(q, ".11f") returns '0.00007748091'
# f"The conductance quantum is {q}" // Returns 'The conductance quantum is 7.748091e-05'
# f"The conductance quantum is {q:.6f}" // Returns 'The conductance quantum is 0.000077'
# Or force smaller: f"quantum is {q:.2e}" // Returns 'quantum is 7.75e-05'

# Subclasses to demo inheritance

class EarthPosition(Position):
	pass


class MarsPosition(Position):
	pass


# Small utility function to return type of object (class) and then name of the object
def typename(obj):
	return type(obj).__name__