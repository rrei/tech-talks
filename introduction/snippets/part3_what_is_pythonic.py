"""Quoted from https://stackoverflow.com/a/25011492/2026122

    Exploiting the features of the Python language to produce code that is clear,
    concise and maintainable.

    Pythonic means code that doesn't just get the syntax right but that follows the
    conventions of the Python community and uses the language in the way it is
    intended to be used.

    This is maybe easiest to explain by negative example (...). Examples of
    unpythonic code often come from users of other languages, who instead of learning
    Python programming patterns such as list comprehensions or generator expressions,
    attempt to crowbar in patterns more commonly used in C or java.

    (...)

    So essentially when someone says something is unpythonic, they are saying that
    the code could be re-written in a way that is a better fit for python's coding
    style.
"""


def example_1():
    ints = [42, 87, 39, 10, 6]

    # unpythonic
    for i in range(0, len(ints)):
        print(ints[i])

    # unpythonic
    for i in ints:
        print(i)


def example_2():
    line = "my furst line"

    # unpythonic
    words = line.split()
    first_word = words[0]
    second_word = words[1]
    third_word = words[2]
    print(third_word, first_word, second_word)

    # pythonic
    first_word, second_word, third_word = line.split()
    print(third_word, first_word, second_word)


def example_3():
    names = ["aLicE", "BOB", "cecIl", "daviD"]

    # VERY unpythonic
    titlecased_names = []
    for i in range(len(names)):
        titlecased_names.append(names[i].title())
    print(titlecased_names)

    # unpythonic
    titlecased_names = []
    for name in names:
        titlecased_names.append(name.title())
    print(titlecased_names)

    # pythonic
    titlecased_names = [name.title() for name in names]
    print(titlecased_names)
