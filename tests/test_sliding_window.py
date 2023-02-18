import pytest

from lib.sliding_window import longest_subarray_sum


@pytest.mark.parametrize(
    'arr,target,expected_max_len', [
        ([3, 1, 2, 7, 4, 2, 1, 1, 5], 8, 4),
        ([3, 5, 2, 7, 1, 4, 2, 1, 1, 5], 8, 4)
    ])
def test_merge_random(arr, target, expected_max_len):
    result = longest_subarray_sum(arr, target)
    assert expected_max_len == result
