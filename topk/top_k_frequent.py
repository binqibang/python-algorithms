from typing import List
import heapq


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    # print(count)
    min_heap = []
    for key, value in count.items():
        if len(min_heap) == k:
            heapq.heappush(min_heap, (value, key))
            heapq.heappop(min_heap)
        else:
            heapq.heappush(min_heap, (value, key))
    return [e[1] for e in min_heap]

