from enum import Enum
import sys
from Color_Console import ctext

#-----------------------------------------------------------------|
#-                                                                |
#-                        Error Handler                           |
#-                                                                |
#-----------------------------------------------------------------|

#* This Just gets the filename of the inputted file
def GetFileName():
	file = ""
	try:
		file = str(sys.argv[1])
		f = (open(file, "r"))
	except:
		file = "text.sol"
		f = open(file, "r")
	return file

#* This Creates Errors and prints them to console
class Error():
	def __init__(self):
		self.file = GetFileName()

	#_ This Throws an error into the console
	def throw(self, errortype, line, message: str = ""):
		if message == "":
			message = errortype.value[1]
		if errortype == ErrorType.InvalidString:
			Error().create(message, line)
		elif errortype == ErrorType.AdditionalInfo:
			Error().create(message, line)
	
	#_ This Creates errors and returns them to be printed
	def create(self, message, line: None):
		ErrorMessage = ""
		if message and line:
			ErrorMessage = f"In {self.file} at line {line}\n    {message}"
		elif message and not line:
			ErrorMessage =  f"In {self.file}\n\    {message}"
		else:
			ErrorMessage = f"In {self.file}"
		Error().senderror(ErrorMessage)
	
	def senderror(self, message):
		ctext(message, text="red", bg="black")

#* Enum Class for ErrorTypes
class ErrorType(Enum):
	InvalidString = (0, "Invalid String Format")
	AdditionalInfo = (1, "Additional Info")
