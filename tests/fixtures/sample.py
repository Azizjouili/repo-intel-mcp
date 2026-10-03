"""A tiny sample module used by the test suite."""


class Greeter:
    def hello(self, name: str) -> str:
        return f"Hello, {name}"


def add(a: int, b: int) -> int:
    return a + b