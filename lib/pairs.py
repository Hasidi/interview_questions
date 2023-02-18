from typing import List


# subsets problem, can use sort

def num_identical_pairs(nums: List[int]) -> int:
    # 1, 2, 2, 5
    # 1, 1, 1, 4
    arr = sorted(nums)
    res = p = 0
    c = 1
    for i in range(1, len(arr)):
        if arr[p] == arr[i]:
            c += 1
        else:
            curr_selection = c * (c-1) // 2  # n choose 2
            c = 1
            p = i
            res += curr_selection
    curr_selection = c * (c - 1) // 2
    res += curr_selection
    return res


def num_identical_pairs_dic(nums: List[int]) -> int:
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = dic.get(nums[i], 0) + 1
    res = sum(c * (c-1) // 2 for c in dic.values())
    return res

