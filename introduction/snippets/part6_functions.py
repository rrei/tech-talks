"""Source: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
"""


def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


ask_ok("Is Python the superior language?")
ask_ok(retries=2, prompt="Is this talk awesome?", reminder="Think carefully...")


def prod(*nums):
    result = 0
    for num in nums:
        result *= num
    return result

prod(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
prod(*range(1, 11))


def artificial_kwargs_example(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}={v}")


artificial_kwargs_example(
    x=False,
    y=42,
    hello="world",
    foo="bar",
)
