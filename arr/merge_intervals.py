from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    intervals.sort(key=lambda i: i[0])
    for interval in intervals:
        if len(merged) == 0:
            merged.append(interval)
        else:
            last = merged[-1]
            if last[1] < interval[0]:
                merged.append(interval)
            else:
                merged.remove(last)
                left = min(last[0], interval[0])
                right = max(last[1], interval[1])
                merged.append([left, right])
    return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
