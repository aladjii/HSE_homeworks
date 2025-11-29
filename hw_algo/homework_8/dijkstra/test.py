import pytest
from main import dijkstra

def test_simple():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2},
        'C': {}
    }
    # Путь A->C = A->B->C = 1 + 2 = 3 (короче, чем прямой 4)
    expected = {'A': 0, 'B': 1, 'C': 3}
    assert dijkstra(graph, 'A') == expected

def test_disconnected_graph():
    graph = {
        'A': {'B': 1},
        'B': {},
        'C': {'D': 1},
        'D': {}
    }
    # Из A можно попасть только в B
    distances = dijkstra(graph, 'A')
    assert distances['A'] == 0
    assert distances['B'] == 1
    assert 'C' not in distances
    assert 'D' not in distances

def test_complex_graph():

    graph = {
        'start': {'a': 6, 'b': 2},
        'a': {'fin': 1},
        'b': {'a': 3, 'fin': 5},
        'fin': {}
    }
    # start -> a (6) -> fin (1) = 7
    # start -> b (2) -> fin (5) = 7
    # start -> b (2) -> a (3) -> fin (1) = 6

    dists = dijkstra(graph, 'start')
    assert dists['fin'] == 6

def test_single_node():
    graph = {'A': {}}
    assert dijkstra(graph, 'A') == {'A': 0}

def test_cycles():
    graph = {
        1: {2: 1},
        2: {1: 1, 3: 5},
        3: {}
    }
    dists = dijkstra(graph, 1)
    assert dists[1] == 0
    assert dists[2] == 1
    assert dists[3] == 6

def test_unreachable_node_handling():
    graph = {
        'A': {'B': 10},
        'B': {},
        'Z': {}
    }
    # Z есть в графе, но из А в него не попасть
    dists = dijkstra(graph, 'A')
    assert 'Z' not in dists
