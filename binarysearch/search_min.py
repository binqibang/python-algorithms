def search_min(nums: list[int]) -> int:
    # 5 6 1 2 3 4
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return nums[i + 1]
    return nums[0]

