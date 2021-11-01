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
		return (
			f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
			f"{abs(self.longitude)}° {self.longitude_hemisphere}"
		)

	def __format__(self, format_spec):
		return "FORMATTED POSITION"
		# Examples: 
		# place = EarthPosition((-10.3, 57.2))
		# f"some sentence {place}" = f"some sentence FORMATTED POSITION"
		# "Another {}".format(place) = "Another FORMATTED POSITION"


# Subclasses to demo inheritance

class EarthPosition(Position):
	pass


class MarsPosition(Position):
	pass


# Small utility function to return type of object (class) and then name of the object
def typename(obj):
	return type(obj).__name__