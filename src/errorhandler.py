from enum import Enum
import sys

#-----------------------------------------------------------------|
#-                                                                |
#-                        Error Handler                           |
#-                                                                |
#-----------------------------------------------------------------|

def GetFileName():
	file = ""
	try:
		file = str(sys.argv[1])
		f = (open(file, "r"))
	except:
		file = "text.sol"
		f = open(file, "r")
	return file

class Error():
	def __init__(self, file):
		self.file = GetFileName()

	def throw(self, errortype, line, message: str = ""):
		print(errortype)
		if errortype.value == ErrorType.InvalidString.value:
			if message == "":
				message = "No Info Provided"
			self.Error.create(message, line)
	
	def create(self, message: str = None, line: str = None):
		if message and line:
			return f"In {self.file} at line {line}\n\t{message}"
		elif message and not line:
			return f"In {self.file}\n\t{message}"
		elif not message and line:
			return f"In {self.file} at line {line}"
		else:
			return f"In {self.file}"

class ErrorType(Enum):
	InvalidString = 0

	def value(self):
		return self.value
