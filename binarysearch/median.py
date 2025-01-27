from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    len1, len2 = len(nums1), len(nums2)

    def get_kth_elem(k):
        # 1 2 3 4
        # 3 4 5 6
        # 1 2 3 3 4 4 5
        p1, p2 = 0, 0
        count = 0
        kth = 0
        while count <= k:
            if p2 == len2 or (p1 < len1 and nums1[p1] < nums2[p2]):
                kth = nums1[p1]
                p1 += 1
            elif p1 == len1 or (p2 < len2 and nums1[p1] >= nums2[p2]):
                kth = nums2[p2]
                p2 += 1
            count += 1
        return kth

    if (len1 + len2) % 2 != 0:
        return get_kth_elem((len1 + len2) // 2)
    else:
        med1 = get_kth_elem((len1 + len2) // 2 - 1)
        med2 = get_kth_elem((len1 + len2) // 2)
        return (med1 + med2) / 2


if __name__ == '__main__':
    arr1 = [1, 3]
    arr2 = [2]
    print(find_median_sorted_arrays(arr1, arr2))
