class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            # Reverse direction when at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Join all rows together
        return "".join(rows)
