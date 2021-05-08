from enum import Enum
class AutoIncrementEnum(Enum): # parent class -- each new enum field has its value incremented
    def __new__(cls,arg): # new(class,argument) -- cls is the class inheriting, arg is the value passed into the unary tuple
        value = len(cls.__members__) # value = however many enum members there are currently (no info would be 0 because there are none, then 1, etc.)
        obj = object.__new__(cls)
        obj._value = value
        obj.outstr = arg # set outstr to the arg inputted
        return obj
class ErrorType(AutoIncrementEnum): # parent class is AutoIncrementEnum which means when __new__ is ran here, it will also carry up to the parent
    def __str__(self):
        return "Error code " + str(self._value) + ": '" + self.outstr + "'"

    InvalidString = ("Invalid String Format")
    AdditionalInfo = ("Additional Info")
