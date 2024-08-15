import bisect
 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        self.nums.insert(bisect.bisect_left(self.nums, val), val)
        return self.nums[self.k-1]