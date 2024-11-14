from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    # 前缀数组，nums[i]左侧所有元素乘积，正向遍历
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # 后缀数组，nums[i]右侧所有元素乘积，反向遍历
    suffix = [1] * n
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    product = [1] * n
    for i in range(n):
        product[i] = prefix[i] * suffix[i]

    return product


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))
