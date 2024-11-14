from typing import List


def partition_labels(s: str) -> List[int]:
    last_idx = dict()
    for i, ch in enumerate(s):
        last_idx[ch] = i
    start = end = 0
    partition = list()
    for i, ch in enumerate(s):
        end = max(end, last_idx[ch])
        if i == end:
            partition.append(end - start + 1)
            start = i + 1
    return partition
