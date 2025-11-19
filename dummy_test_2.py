# Another dummy file for testing PyGithub PR diff
# This file can be deleted after testing

class Calculator:
    """A simple calculator class."""

    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self

    def subtract(self, value):
        self.result -= value
        return self

    def multiply(self, value):
        self.result *= value
        return self

    def get_result(self):
        return self.result

    def reset(self):
        self.result = 0
        return self


if __name__ == "__main__":
    calc = Calculator()
    result = calc.add(10).subtract(3).multiply(2).get_result()
    print(f"Result: {result}")

