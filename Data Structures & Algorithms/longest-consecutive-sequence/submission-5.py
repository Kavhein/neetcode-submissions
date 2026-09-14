class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)

        max_count = 0
        for i in s1:
            if i-1 not in s1:
                count = 1
                new_number = i+1
                while new_number in s1:
                    count += 1
                    new_number += 1
                max_count = max(max_count, count)
    
        return max_count