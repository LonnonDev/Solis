from enum import Enum

#-----------------------------------------------------------------|
#-                                                                |
#-                           ErrorType                            |
#-                                                                |
#-----------------------------------------------------------------|

#* Parent Class -- each new enum member has its value incremented
class AutoIncrementEnum(Enum): 
	#* new(class,argument) -- cls is the class inheriting, arg is the value passed into the unary tuple
	def __new__(cls,arg):
		#_ Value = However many enum members there are currently (INVALID_STRING would be 0 because there are none, then ADDITIONAL_INFO 1, etc.)
		value = len(cls.__members__)
		obj = object.__new__(cls)
		obj._value = value
		#_ Value2 is set to arg.
		obj.value2 = arg
		return obj
#* Parent class is AutoIncrementEnum which means when __new__ is ran here (ie. by each enum member), it will also carry up to the parent
class ErrorType(AutoIncrementEnum):
	def __str__(self):
		return "Error code " + str(self._value) + ": '" + self.value2 + "'"

	INVALID_STRING = ("Invalid String Format")
	ADDITIONAL_INFO = ("Additional Info")
