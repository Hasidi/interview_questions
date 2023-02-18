from lib.helpers import rand_arr
from lib.pairs import num_identical_pairs_dic, num_identical_pairs


def test_num_identical_pairs():
    for i in range(10):
        arr = rand_arr(max_n=100, max_len=20, min_len=10)
        expected = num_identical_pairs_dic(arr)
        res = num_identical_pairs(arr)
        assert res == expected, f'Failed in {sorted(arr)}'