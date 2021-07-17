n = None  # usually used to represent "nothing" (eq. NULL)
b = False  # actual booleans, not zeros and ones!
i = 5 ** 500  # integers with arbitrary precision
f = 3.14  # decent approximation of real numbers
s = "hello"  # strings (characters are simply 1-char-long strings)
T = (0, 0)  # immutable ordered sequence of objects of any type
L = [10, 4]  # mutable ordered sequence of objects of any type
D = {"key": "value"}  # (hash table based) associated array
S = {"dog", "cat", "snake"}  # (hash table based) set

# Usage examples:
# n is None
# b or not b
# i // 2
# f / 2
# s[1:-1].upper()
# T[0]
# L.append("roger")
# D["key"]
# "snake" in S
