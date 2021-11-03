import re
from yaml import load
from yaml.loader import FullLoader
from collections.abc import Mapping


class Content(Mapping):
	__delimeter = "^(?:-|\+){3}\s*$"

	__regex = re.compile(__delimeter, re.MULTILINE)

	@classmethod
	def load(self, cls, string):
		_, fm, content = __regex.split(string, 2)
		load(fm, Loader=FullLoader)
		return cls(metadata, content)

	def __init__(self, metadata, content):
		self.data = metadata
		self.data("content") = content
	
	@property
	def body(self):
		return self.data["content"]
	
	@property
	def type(self):
		self.data.has_key(type) ? self.data["type"] : None