def merge_sort(arr):

    def msort(arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        msort(arr, low, mid)
        msort(arr, mid + 1, high)
        merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        tmp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1
        while i <= mid:
            tmp.append(arr[i])
            i += 1
        while j <= high:
            tmp.append(arr[j])
            j += 1
        for k in range(low, high + 1):
            arr[k] = tmp[k - low]

    msort(arr, 0, len(arr) - 1)
    return arr
