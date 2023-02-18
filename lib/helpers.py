import random
from typing import List


def rand_arr(max_n=5001, max_len=40, min_len=20) -> List[int]:
    if max_len < min_len:
        min_len = max_len
    arr = [random.randint(1, max_n) for _ in range(random.randint(min_len, max_len+1))]
    return arr
