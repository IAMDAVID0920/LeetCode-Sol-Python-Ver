# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

#Implement the TwoSum class:

# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false

class TwoSum:

    def __init__(self):
        self.res = []

    def add(self, number: int) -> None:
        self.res.append(number)

    def find(self, value: int) -> bool:
        # contain the set with all diff values
        complement = set()
        for num in self.res:
            if value - num in complement:
                return True

            complement.add(num)

        return False

# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(3)
obj.add(4)
obj.add(7)
obj.add(10)
param_2 = obj.find(11)
print(param_2)
