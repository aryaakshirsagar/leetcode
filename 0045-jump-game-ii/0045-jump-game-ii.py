class Solution:
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        # we don't need to jump from the last index
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        return jumps

# quick local test (not needed on LeetCode)
if __name__ == "__main__":
    print(Solution().jump([2,3,1,1,4]))  # expected 2
    print(Solution().jump([2,3,0,1,4]))  # expected 2
