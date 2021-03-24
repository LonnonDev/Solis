# Solis #
Solis is a programming language made for fun in Python.

Releases [Here.](https://github.com/LonnonDev/Solis/releases)
  
  <a href="https://github.com/LonnonDev/Solis/issues">
    <img alt="contributions welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat">
  </a>

# Features #
There is a Lexer and a Tokeninator

  ## Lexer ##
  - The lexer makes it so that it can process the code and put it into a list and then you can pass it to the tokeninator
  - For example ```out "Hello, World!"``` would be ```["out", '"', '"']```
  - The Lexer also takes the Lexed list and converts it into a list with lists in it saying what type of data is this
  - For example ```["out", '"', '"']``` would be ```[["out", "FUNC"], ['"', "STRING"], ['"', "STRING"]]```
