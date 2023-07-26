import random
from typing import Dict, List


# class RandomizedSet:

#     def __init__(self):
#         self.set : List = []
        

#     def insert(self, val: int) -> bool:
#         if val in self.set:
#             return False
#         self.set.append(val)
#         return True
        

#     def remove(self, val: int) -> bool:
#         if val in self.set:
#             self.set.remove(val)
#             return True
#         else:
#             return False
        

#     def getRandom(self) -> int:
#         return random.choice(self.set)

class RandomizedSet:

    def __init__(self):
        self.registration : Dict = {}
        self.data : List = []
        self.size = 0
        

    def insert(self, val: int) -> bool:
        if val in self.registration:
            return False
        self.registration[val] = self.size
        self.data.append(val)
        self.size += 1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.registration:
            last = self.data[-1]
            index_to_remove = self.registration[val]
            self.data[index_to_remove] = last
            self.registration[last] = index_to_remove
            self.data.pop()
            self.size -= 1
            self.registration.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_2 = obj.remove(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
