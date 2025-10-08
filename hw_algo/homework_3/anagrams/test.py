import pytest
from anagrams import group_anagrams


@pytest.mark.parametrize(
    "strs, expected_groups",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (["abc"], [["abc"]]),
        (["a", "a", "a"], [["a", "a", "a"]]),
        (["ab", "cd", "ef"], [["ab"], ["cd"], ["ef"]]),
        (["", "b", ""], [["", ""], ["b"]]),
    ],
)
def test_group_anagrams(strs, expected_groups):
    result = list(group_anagrams(strs))
    assert {tuple(g) for g in result} == {tuple(g) for g in expected_groups}
