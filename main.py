"""
My best project.
"""


def my_sub(a: int, b: int) -> int:
    return a - b


def my_add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(f"{1} + {2} = {my_add(1, 2)}")
    print(f"{2} - {1} = {my_sub(2, 1)}")
