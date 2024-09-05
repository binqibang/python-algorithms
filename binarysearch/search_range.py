def search(nums, target, flag):
    start, end = 0, len(nums) - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            res = mid
            if flag:
                end = mid - 1
            else:
                start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return res


def search_range(nums: list[int], target: int) -> list[int]:
    l_range = search(nums, target, 1)
    r_range = search(nums, target, 0)
    return [l_range, r_range]
