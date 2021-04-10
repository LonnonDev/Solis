# Solis #
Solis is an Object Oriented programming language made for fun in Python.

Releases [Here.](https://github.com/LonnonDev/Solis/releases)
  
  <a href="https://github.com/LonnonDev/Solis/issues">
    <img alt="contributions welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat">
  </a>

# Features #
There is a Lexer and a Parser

## Lexer ##
  - The lexer makes it so that it can process the code and put it into a list and then you can pass it to the tokeninator
  - For example ```out "Hello, World!"``` would be ```["out", '"', "Hello, World!", '"']```
  - The Lexer also takes the Lexed list and tokenizes it.
  - For example ```["out", '"', "Hello, World!", '"']``` would be ```[["out", "FUNC"], ['"', "STRING"], ["Hello, World!", "STRING"] ['"', "STRING"]]```

## Parser ##
  - The parser looks at the Tokenized List and does operation and runs functions.
  - For example ```[["out", "FUNC"], ['"', "STRING"], ["Hello, World!", "STRING"] ['"', "STRING"]]``` would print ```Hello, World!"```
