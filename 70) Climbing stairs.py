class Solution:
    def __init__(self):
        self.dct = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if not n in self.dct:
            self.dct[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dct[n]