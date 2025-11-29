def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            stack = [node]
            visited.add(node)

            while stack:
                current = stack.pop()
                component.append(current)

                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            components.append(component)

    return components
