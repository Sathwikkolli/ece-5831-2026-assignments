"""pythontutorial.net - Python Basics, Section 11: More on Functions

Topics: unpacking tuples, *args, **kwargs, partial functions, type hints.
Run with:  python python-tutorial-11.py
"""
from functools import partial
from typing import Union


def section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------------ unpacking tuples
section("1. Unpacking tuples")

point = 10, 20            # packing
x, y = point              # unpacking
print(f"x = {x}, y = {y}")

x, y = y, x               # swapping two variables
print(f"after swap: x = {x}, y = {y}")

r, g, *other = (192, 210, 100, 0.5)
print(f"r = {r}, g = {g}, other = {other}")

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
numbers = (*odd_numbers, *even_numbers)
print("merged tuple:", numbers)

try:
    a, b = (1, 2, 3)
except ValueError as error:
    print("ValueError:", error)


# ------------------------------------------------------------------ *args
section("2. *args")


def add(*args):
    print("args is a", type(args).__name__, args)
    total = 0
    for arg in args:
        total += arg
    return total


print("add(1, 2, 3) =", add(1, 2, 3))
print("add() =", add())


def add_with_first(x, y, *args):
    return x + y + sum(args)


print("add_with_first(1, 2, 3, 4) =", add_with_first(1, 2, 3, 4))


def add_keyword_after(*numbers, z):
    return sum(numbers) + z


print("add_keyword_after(10, 20, z=30) =", add_keyword_after(10, 20, z=30))


def point_str(a, b):
    return f"({a}, {b})"


pt = (0, 0)
print("unpacking into args:", point_str(*pt))


# ------------------------------------------------------------------ **kwargs
section("3. **kwargs")


def connect(**kwargs):
    print("kwargs is a", type(kwargs).__name__)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


connect(server="localhost", port=3306, user="root", password="Py1hon!Xt12")


def connect_with_defaults(fn, *args, **kwargs):
    print(f"fn={fn}, args={args}, kwargs={kwargs}")


connect_with_defaults("mysql", "localhost", port=3306, user="root")

config = {"server": "localhost", "port": 3306}
connect(**config)  # unpacking a dict into keyword arguments


# ------------------------------------------------------------------ partial functions
section("4. Partial functions")


def multiply(a, b):
    return a * b


double = partial(multiply, b=2)
triple = partial(multiply, b=3)
print("double(10) =", double(10))
print("triple(10) =", triple(10))

to_int_base2 = partial(int, base=2)
print("to_int_base2('1011') =", to_int_base2("1011"))

# a partial remembers its function and arguments
print("double.func =", double.func.__name__, "keywords =", double.keywords)


# ------------------------------------------------------------------ type hints
section("5. Type hints")


def say_hi(name: str) -> str:
    return f"Hi {name}"


greeting = say_hi("John")
print(greeting)


def add_numbers(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


print("add_numbers(1, 2.5) =", add_numbers(1, 2.5))

number = 12  # int inferred
price: float = 9.99
rating: list[int] = [1, 2, 3]
ratings: dict[str, int] = {"Manager": 2, "Lead": 1}
print("annotations of add_numbers:", add_numbers.__annotations__)

# type hints are not enforced at runtime (a type checker such as mypy would flag this)
print("say_hi(123) still runs:", say_hi(123))
