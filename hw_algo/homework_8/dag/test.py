import pytest
from main import process_dag

def test1():
    # 1 -> 2 -> 3
    graph = {
        1: [2],
        2: [3],
        3: []
    }
    res = process_dag(graph)
    assert res["has_cycle"] is False
    assert res["topo_sort"] == [1, 2, 3]

def test2():
    #   /-> 2 ->\
    # 1          4
    #   \-> 3 ->/
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    res = process_dag(graph)
    assert res["has_cycle"] is False
    # Топологическая сортировка может быть [1, 3, 2, 4] или [1, 2, 3, 4]
    ts = res["topo_sort"]
    assert ts.index(1) < ts.index(2)
    assert ts.index(1) < ts.index(3)
    assert ts.index(2) < ts.index(4)
    assert ts.index(3) < ts.index(4)

def test_cycle():
    # 1 -> 2 -> 1
    graph = {
        1: [2],
        2: [1]
    }
    res = process_dag(graph)
    assert res["has_cycle"] is True
    assert set(res["cycle"]) == {1, 2}

def test_self_loop():
    # 1 -> 1
    graph = {
        1: [1],
        2: []
    }
    res = process_dag(graph)
    assert res["has_cycle"] is True
    assert res["cycle"] == [1]

def test_cycle_in_middle():
    # 1 -> 2 -> 3 -> 4 -> 2
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [2]
    }
    res = process_dag(graph)
    assert res["has_cycle"] is True
    cycle = res["cycle"]
    assert 1 not in cycle
    assert len(cycle) == 3
    assert set(cycle) == {2, 3, 4}

def test_disconnected_components():
    # 1->2   3->4
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    res = process_dag(graph)
    assert res["has_cycle"] is False
    ts = res["topo_sort"]
    assert len(ts) == 4
    assert ts.index(1) < ts.index(2)
    assert ts.index(3) < ts.index(4)

def test_complex_cycle():
    graph = {
        1: [2],
        2: [3, 4],
        3: [1],
        4: [5],
        5: [4]
    }
    res = process_dag(graph)
    assert res["has_cycle"] is True
    c = set(res["cycle"])
    assert c == {1, 2, 3} or c == {4, 5}
