import heapq

def dijkstra(graph, start):
    distances = {start: 0}
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances.get(current_node, float('inf')):
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
