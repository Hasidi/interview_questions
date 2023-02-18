import pytest

from lib.helpers import rand_arr
from lib.pointers import merge, is_subsequence, find_target_sum


@pytest.mark.parametrize(
    'a,b', [
        (rand_arr(), rand_arr()),
        ([1, 4, 5, 7], [2, 6, 8])
    ])
def test_merge_random(a, b):
    result = merge(sorted(a), sorted(b))
    expected = sorted(a + b)
    assert expected == result


@pytest.mark.parametrize(
    's1,s2,expected', [
        ('abcde', 'ace', True),
        ('abcde', 'ake', False),
        ('a6', 'k5ab6', True),
    ])
def test_is_subsequence(s1, s2, expected):
    assert is_subsequence(s1, s2) == expected


@pytest.mark.parametrize(
    'a,target, expected', [
        ([1, 2, 5, 6, 9], 11, (1,4)),
        ([3, 2, 5, 6, 10], 11, (2,3)),
    ])
def test_target_sum(a, target, expected):
    assert find_target_sum(a, target) == expected
