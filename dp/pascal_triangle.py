from typing import List


def generate(num_rows: int) -> List[List[int]]:
    prev_row = [1]
    ans = [prev_row]
    for i in range(2, num_rows + 1):
        curr_row = [0] * i
        for j in range(0, i):
            left_top = prev_row[j - 1] if j - 1 >= 0 else 0
            right_top = prev_row[j] if j < i - 1 else 0
            curr_row[j] = left_top + right_top
        prev_row = curr_row
        ans.append(curr_row)
    return ans
