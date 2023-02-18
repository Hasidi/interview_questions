from typing import List


def partition(arr: List[int], left: int, right: int, pivot_idx: int):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot: # while bigger we skip until we find smaller and swap it with last bigger
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr: List[int]):
    def _quick_sort(left: int, right: int):
        if left >= right:
            return arr
        # pivot = random.randint(left, right)
        pivot = right
        p = partition(arr, left, right, pivot)
        _quick_sort(left, p - 1)
        _quick_sort(p + 1, right)
        return arr
    return _quick_sort(0, len(arr)-1)
