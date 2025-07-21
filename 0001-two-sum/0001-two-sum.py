class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # to store number and its index

        for i, n in enumerate(nums):
            diff = target - n  # the number we need to find
            if diff in hashmap:
                return [hashmap[diff], i]  # found the pair
            hashmap[n] = i  # store index of current number
