from typing import List, Optional, Tuple


# for subsequence problems (portion of an array that keeps order but doesn't need to be contiguous
# - use pointers (or dynamic programming)

def merge(l1: List[int], l2: List[int]):
    i = j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    res = res + l2[j:] if i >= len(l1) else res + l1[i:]
    return res


def is_subsequence(s1: str, s2: str):
    i = j = 0
    if len(s1) >= len(s2):
        l1 = s1
        l2 = s2
    else:
        l1 = s2
        l2 = s1
    while i < len(l1):
        if l1[i] == l2[j]:
            j += 1
        i += 1
    return True if j == len(l2) else False


def find_target_sum(arr: List[int], target: int) -> Tuple[Optional[int], Optional[int]]:
    # can be solved with dictionary in a linear time
    a = sorted(arr)
    i = 0
    j = len(a) - 1
    while i < len(a) - 1 and j > 0:
        curr_sum = a[i] + a[j]
        if curr_sum == target:
            return i, j
        if a[i] + a[j] > target:
            j -= 1
        else:
            i += 1
    return None, None
