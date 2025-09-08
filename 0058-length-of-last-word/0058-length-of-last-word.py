class Solution(object):
    def lengthOfLastWord(self, s):
        # Strip trailing spaces, then split by spaces
        words = s.strip().split(" ")
        return len(words[-1])
