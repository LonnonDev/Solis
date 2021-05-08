import sys
from Color_Console import ctext

from src.errortype import ErrorType
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

class Error(): # class containing ErrorType, and maybe file and line if needed
    def __init__(self,err,line=None,file=None): # initializer, takes ErrorType and optionally file and line
        if isinstance(err,ErrorType): # if err is an ErrorType, do shit
            self.err = err   #set fields equal to initializer values
            self.file = file or GetFileName()
            self.line = line
        else: #if not, don't
            raise TypeError("Error(err,file,line) -- type of err must be ErrorType enum!")
    def __str__(self): # how should it be str()'d
        if self.file is None and self.line is None: # if no file and no line,
            return f"Error:\n    {str(self.err)}" # just return str'd error
        elif self.line is None: # if no line
            return f"Error in file '{self.file}'\n    {str(self.err)}"
        else: #if line and file (or just line but that wouldn't normally occur)
            return f"Error in file '{self.file}' on line {str(self.line)}\n    {str(self.err)}"
    def errout(self): # errout just prints str'd itself
        ctext(str(self),text="red",bg="black")
