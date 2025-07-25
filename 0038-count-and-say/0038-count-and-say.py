class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = "1"

        for _ in range(2, n + 1):
            current = ""
            count = 1
            prev = result[0]

            for char in result[1:]:
                if char == prev:
                    count += 1
                else:
                    current += str(count) + prev
                    count = 1
                    prev = char

            # Add the last group
            current += str(count) + prev
            result = current

        return result
