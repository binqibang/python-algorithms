def top_k_largest(nums: list[int], k: int) -> int:
    def find(nums: list[int], start: int, end: int, pos: int):
        pivot = nums[start]
        i, j = start, end
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[i] = nums[i], nums[start]
        if i == pos:
            return pivot
        elif i < pos:
            return find(nums, i + 1, end, pos)
        else:
            return find(nums, start, i - 1, pos)

    # 1 2 3 4 5 6 7  3
    pos = len(nums) - k
    return find(nums, 0, len(nums) - 1, pos)
