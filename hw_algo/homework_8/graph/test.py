import pytest
from main import find_connected_components

def normalize(components):
    return sorted([sorted(c) for c in components])

def test_simple_two_components():
    graph = {
        1: [2],
        2: [1],
        3: []
    }
    result = find_connected_components(graph)
    assert normalize(result) == [[1, 2], [3]]

def test_linear_graph():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3]
    }
    result = find_connected_components(graph)
    assert normalize(result) == [[1, 2, 3, 4]]

def test_fully_disconnected():
    graph = {
        1: [],
        2: [],
        3: []
    }
    result = find_connected_components(graph)
    assert normalize(result) == [[1], [2], [3]]

def test_cycle():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    result = find_connected_components(graph)
    assert normalize(result) == [[1, 2, 3]]

def test_empty():
    graph = {}
    result = find_connected_components(graph)
    assert result == []

def test_singlenode():
    graph = {1: []}
    result = find_connected_components(graph)
    assert normalize(result) == [[1]]

def test_complex():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3, 5],
        5: [4],
        6: []
    }
    result = find_connected_components(graph)
    assert normalize(result) == [[1, 2], [3, 4, 5], [6]]
