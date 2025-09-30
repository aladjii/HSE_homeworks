import pytest
from listnode import list_to_linked, linked_to_list
from merge_dummy import merge_dummy
from merge import merge


@pytest.mark.parametrize("list1, list2, expected", [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [0], [0]),
    ([2], [], [2]),
    ([], [], []),
    ([1,3,5], [2,4,6], [1,2,3,4,5,6]),
])
def test_merge_with_dummy(list1, list2, expected):
    l1 = list_to_linked(list1)
    l2 = list_to_linked(list2)
    merged = merge_dummy(l1, l2)
    assert linked_to_list(merged) == expected


@pytest.mark.parametrize("list1, list2, expected", [
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [0], [0]),
    ([2], [], [2]),
    ([], [], []),
    ([1,3,5], [2,4,6], [1,2,3,4,5,6]),
])
def test_merge_without_dummy(list1, list2, expected):
    l1 = list_to_linked(list1)
    l2 = list_to_linked(list2)
    merged = merge(l1, l2)
    assert linked_to_list(merged) == expected
