def quick_sort(arr: list[int]) -> list[int]:
    def partition(arr: list[int], low: int, high: int):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            while i < j and arr[i] <= pivot:
                i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[i] = arr[i], arr[low]
        return i

    def qsort(arr: list[int], low: int, high: int):
        if low >= high:
            return
        mid = partition(arr, low, high)
        qsort(arr, low, mid - 1)
        qsort(arr, mid + 1, high)
        
    qsort(arr, 0, len(arr) - 1)
    return arr
