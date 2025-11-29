import pytest
from main import rabin_karp_search

def test1():
    text = "hello world"
    pattern = "world"
    assert rabin_karp_search(text, pattern) == 6

def test2():
    text = "hello world"
    pattern = "hello"
    assert rabin_karp_search(text, pattern) == 0

def test3():
    text = "hello world"
    pattern = "python"
    assert rabin_karp_search(text, pattern) == -1

def test4():
    text = "hi"
    pattern = "hello"
    assert rabin_karp_search(text, pattern) == -1

def test5():
    text = "anything"
    pattern = ""
    assert rabin_karp_search(text, pattern) == 0

def test6():
    text = "AAAAAB"
    pattern = "AAAB"
    assert rabin_karp_search(text, pattern) == 2

def test7():
    text = "Привет мир"
    pattern = "мир"
    assert rabin_karp_search(text, pattern) == 7

def test8():
    text = "abc"
    pattern = "abc"
    assert rabin_karp_search(text, pattern) == 0
