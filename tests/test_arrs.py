import pytest

from utils import arrs


@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 2),
    ([1, 2, 3], -1, "test", "test")
])
def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected
    with pytest.raises(IndexError):
        arrs.get([], 0, "test") == "test"


@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([], 1, None, []),
    ([1, 2, 3], -1, None, [3]),
    ([1, 2, 3], -4, None, [1, 2, 3])
])
def test_slice(coll, start, end, expected):
    assert arrs.my_slice(coll, start, end) == expected
