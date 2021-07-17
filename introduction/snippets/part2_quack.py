"""
Source: https://www.geeksforgeeks.org/type-systemsdynamic-typing-static-typing-duck-typing/

Duck Typing is a concept related to Dynamic Typing, where the type or the class of an
object is less important than the method it defines. Using Duck Typing, we do not
check types at all. Instead we check for the presence of a given method or attribute.
The reason behind the name is the duck test: "If it looks like a duck, swims like a
duck, and quacks like a duck, then it probably is a duck".
"""

a = "hello"
print(type(a))

a = 5
print(type(a))


def add(a, b):
    return a + b


print(add("hello", "world"))
print(add(2, 4))
print(add(["foo"], ["bar", True]))
