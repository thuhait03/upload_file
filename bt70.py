import csv
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        return b


with open("config.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    row = next(reader)
    n = int(row["n"])
    print("n =", n)
