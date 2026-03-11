from collections import Counter
import math 

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum()/self.count()
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())  # 25
print('Sum:', data.sum())  # 744
print('Min:', data.min())  # 24
print('Max:', data.max())  # 38
print('Range:', data.range())  # 14
print('Mean:', data.mean())  # 29.76 ~ 30