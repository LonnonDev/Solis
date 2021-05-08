
#-----------------------------------------------------------------|
#-                                                                |
#-                        Error Handler                           |
#-                                                                |
#-----------------------------------------------------------------|

class Error():
    def throw(self, errortype, file, line, message: str = ""):
        if errortype == 0x00:
            if message == "":
                message = "No Info Provided"
            Error.create(file, message, line)
    
    def create(self, file, message, line):
        return f"""
In {file} at line {line},
    {message}
"""
