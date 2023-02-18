# subarray/substring problem - use sliding window
from typing import List


def longest_subarray_sum(nums: List[int], t: int):
    p = s = result = 0
    a = []
    for i in range(len(nums)):
        s += nums[i]
        # good solution #
        while s > t:
            s -= nums[p]
            p += 1
        if s == t:
            a.append((p, i))
            result = max(result, i - p + 1)
        # wrong solution #
        # if s > t:
        #     s -= nums[p]
        #     p += 1
        #     if s == t:
        #         a.append((p, i))
        # elif s == t:
        #     a.append((p, i))
        #     result = max(result, i - p + 1)
        #     s -= nums[p]
        #     p = i
    return result
