from lib.helpers import rand_arr
from lib.sorting import quick_sort


def test_quick_sort_one():
    arr = [10, 80, 90, 30, 100, 40, 50, 70]
    assert sorted(arr) == quick_sort(arr)

def test_quick_sort():
    for i in range(100):
        arr = rand_arr()
        expected = sorted(arr)
        quick_sort(arr)
        assert arr == expected

