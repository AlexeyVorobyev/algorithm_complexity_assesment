import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

def create_graph(num_vertices, edge_probability):
    graph = nx.Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() <= edge_probability:
                graph.add_edge(i, j)
    return graph

num_vertices = 10
edge_probability = 0.5

graph = create_graph(num_vertices, edge_probability)

def get_adjacency_matrix(graph):
    num_vertices = len(graph.nodes)
    adjacency_matrix = np.zeros((num_vertices, num_vertices))
    for edge in graph.edges:
        adjacency_matrix[edge[0], edge[1]] = 1
        adjacency_matrix[edge[1], edge[0]] = 1
    return adjacency_matrix

# Вывод матрицы сложности графа
adjacency_matrix = get_adjacency_matrix(graph)
print("Adjacency Matrix:")
print(adjacency_matrix)

def longest_path_exact(graph, start, end):
    longest = []
    paths = nx.all_simple_paths(graph, start, end)
    for path in paths:
        if len(path) > len(longest):
            longest = path
    return longest

def longest_path_greedy(graph, start, end):
    path = [start]
    current = start
    while current != end:
        neighbors = list(graph[current])
        if not neighbors:
            return None
        next_vertex = max(neighbors, key=lambda v: len(graph[v]))
        graph.remove_edge(current, next_vertex)
        path.append(next_vertex)
        current = next_vertex
    return path

def longest_path_random(graph, start, end, iterations=1000):
    best_path = None
    best_length = 0
    for _ in range(iterations):
        current = start
        path = [current]
        length = 0
        while current != end:
            neighbors = list(graph[current])
            if not neighbors:
                break
            next_vertex = random.choice(neighbors)
            graph.remove_edge(current, next_vertex)
            path.append(next_vertex)
            current = next_vertex
            length += 1
        if length > best_length:
            best_path = path
            best_length = length
        # Восстановление исходного графа
        for vertex in path[:-1]:
            graph.add_edge(vertex, path[-1])
    return best_path

def longest_path_approximation(graph, start, end):
    path = [start]
    current = start
    while current != end:
        neighbors = list(graph[current])
        if not neighbors:
            return None
        next_vertex = random.choice(neighbors)
        graph.remove_edge(current, next_vertex)
        path.append(next_vertex)
        current = next_vertex
    return path

num_vertices = 10
edge_probability = 0.5

graph = create_graph(num_vertices, edge_probability)
start = random.randint(0, num_vertices - 1)
end = random.randint(0, num_vertices - 1)
while end == start:
    end = random.randint(0, num_vertices - 1)

print("Граф:")
print(graph.edges())

print("\nТочный алгоритм:")
exact_path = longest_path_exact(graph.copy(), start, end)
if exact_path:
    print("Самый длинный путь:", exact_path)
    print("Длина:", len(exact_path))
else:
    print("Путь не найден.")

print("\nЖадный алгоритм:")
greedy_path = longest_path_greedy(graph.copy(), start, end)
if greedy_path:
    print("Самый длинный путь:", greedy_path)
    print("Длина:", len(greedy_path))
else:
    print("Путь не найден.")

print("\nСлучайный алгоритм:")
random_path = longest_path_random(graph.copy(), start, end)
if random_path:
    print("Самый длинный путь:", random_path)
    print("Длина:", len(random_path))
else:
    print("Путь не найден.")

print("\nАлгоритм аппроксимации:")
approx_path = longest_path_approximation(graph.copy(), start, end)
if approx_path:
    print("Самый длинный путь:", approx_path)
    print("Длина:", len(approx_path))
else:
    print("Путь не найден.")

# Визуализация графа
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')

# Выделение пути, полученного с помощью точного алгоритма
if exact_path:
    for i in range(len(exact_path) - 1):
        nx.draw_networkx_edges(graph, pos, edgelist=[(exact_path[i], exact_path[i + 1])], edge_color='green', width=2)

plt.show()
