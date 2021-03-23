# Solis #
Solis is a programming language made for fun in Python.

# Features #
There is a Lexer and a Tokeninater

  ## Lexer ##
  - The lexer makes it so that it can process the code and put it into a list and then you can pass it to the tokeninator
  - For example ```out "Hello, World!"``` would be ```["out", '"', '"']```
  ## Tokeninator ##
  - The tokeninator takes the Lexed list and converts it into a list with lists in it saying what type of data is this
  - For example ```py
  ["out", '"', '"']``` would be ```[["out", "FUNC"], ['"', "STRING"], ['"', "STRING"]]```

# Releases #
Releases can be found here [Releases](https://github.com/LonnonDev/Solis/releases)
