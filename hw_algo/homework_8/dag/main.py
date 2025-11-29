WHITE = 0
GRAY = 1
BLACK = 2

def process_dag(graph):
    state = {node: WHITE for node in graph}
    parent = {}
    topo_order = []

    result = {
        "has_cycle": False,
        "cycle": [],
        "topo_sort": []
    }
    all_nodes = list(graph.keys())

    def dfs(u):
        state[u] = GRAY
        for v in graph.get(u, []):
            if state.get(v, WHITE) == GRAY:
                cycle_path = [u]
                curr = u

                while curr != v:
                    curr = parent[curr]
                    cycle_path.append(curr)

                cycle_path.reverse()
                return cycle_path

            if state.get(v, WHITE) == WHITE:
                parent[v] = u
                cycle_found = dfs(v)
                if cycle_found:
                    return cycle_found

        state[u] = BLACK
        topo_order.append(u)
        return None

    for node in all_nodes:
        if state[node] == WHITE:
            cycle = dfs(node)
            if cycle:
                result["has_cycle"] = True
                result["cycle"] = cycle
                return result

    result["topo_sort"] = topo_order[::-1]
    return result
