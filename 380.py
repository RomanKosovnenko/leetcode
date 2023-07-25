import random
from typing import List


class RandomizedSet:

    def __init__(self):
        self.set : List = []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_2 = obj.remove(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
