class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for num in my_set:
            x = num
            if x-1 not in my_set:
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest

        