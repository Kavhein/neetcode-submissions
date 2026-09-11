class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            seen.add(i)
        print(seen)
        if len(seen) == len(nums):
            return False
        else:
            return True
        