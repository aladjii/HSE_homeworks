import pytest
from main import lcs

def test1():
    string_1 = "AGGTAB"
    string_2 = "GXTXAYB"
    assert lcs(string_1, string_2) == "GTAB"

def test2():
    assert lcs("hello", "hello") == "hello"

def test3():
    assert lcs("abc", "def") == ""

def test4():
    assert lcs("", "abc") == ""
    assert lcs("abc", "") == ""

def test5():
    assert lcs("ABC", "AZBZC") == "ABC"

def test6():
    res = lcs("AB", "BA")
    assert res == "A" or res == "B"

def test7():
    s1 = "A" * 50 + "B"
    s2 = "A" * 50 + "C"
    assert len(lcs(s1, s2)) == 50
