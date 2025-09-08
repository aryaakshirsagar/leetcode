class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last = {}          # char -> last seen index
        start = 0          # left edge of window
        best = 0
        for i, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                start = last[ch] + 1     # jump left past the repeat
            last[ch] = i
            best = max(best, i - start + 1)
        return best
