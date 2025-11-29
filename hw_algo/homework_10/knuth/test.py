import pytest
from main import kmp_search

def test1():
    text = "sadbutsad"
    pattern = "sad"
    assert kmp_search(text, pattern) == 0

def test2():
    text = "hello world"
    pattern = "world"
    assert kmp_search(text, pattern) == 6

def test3():
    text = "leetcode"
    pattern = "python"
    assert kmp_search(text, pattern) == -1

def test4():
    assert kmp_search("abc", "") == 0

def test5():
    assert kmp_search("abc", "abcdef") == -1

def test6():
    text = "AAAAAB"
    pattern = "AAAB"
    assert kmp_search(text, pattern) == 2

def test7():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert kmp_search(text, pattern) == 10
