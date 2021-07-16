# An introduction to Python
## Squeezing the serpent to create Life

### Abstract
In this session we'll introduce the Python programming language and cover the basics of 
its syntax, a few essential built-in functions and a couple of more advanced features. 
Then, we'll use our newly found knowledge to recreate Conway's Game of Life leveraging 
Python's extensive standard library.

### Prerequisites
- basic notions of imperative and object-oriented programming
- no Python knowledge is assumed

### Outline
- Philosophy:
    - Zen of Python
    - pythonic code
    - multi-paradigm
    - duck typing
    - batteries included 
- Basics:
    - Interactive Interpreter: python and ipython
    - Variables: references, not values!
    - Builtin Types:
        - None
        - bool
        - int
        - float
        - str
        - tuple (not common in other languages)
        - list
        - dict
        - set
    - Syntax:
        - assignment (regular, augmented, unpacking, chained)
        - arithmetic (+, -, *, /, //, %, **)
        - boolean (and, or, not)
        - bitwise (&, |, ^, ~, <<, >>)
        - comparison (==, !=, <, <=, >, >=, chaining)
        - membership (in, not in)
        - identity (is, is not)
        - indexing and slicing (x[i], x[i:j:k])
        - ternary (if-else)
        - deletion (del)
        - f-strings
        - indentation-based blocks
        - if/elif/else (truthyness and falsyness)
        - while/for
        - break/continue
        - try/except/finally
        - assert
        - def
        - return
        - class
        - from/import
        - modules and packages
    - Builtin Functions: print, range, len, min, max, sum, all, any, type, isinstance
- Functions:
    - default values
    - named arguments
    - returning multiple values
    - everything is an object
    - lambdas, higher-order functions, FP
- Classes:
    - no, really, EVERYTHING is an object
    - instance methods (self - because explicit is better than implicit)
    - magic methods and operator overloading
- Conway's Game of Life:
    - implementing the rules
    - displaying our grid
    - building a UI
