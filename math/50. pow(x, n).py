class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return self.pow(x, n)
    
    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = self.pow(x, n // 2)
        if n % 2 == 1:
            return temp * temp
        else:
            return temp * temp * x
