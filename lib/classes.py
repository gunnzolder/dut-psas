from collections import deque

class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacency_list = []

    def add_neighbor(self, vertex):
        self.adjacency_list.append(vertex)

    def __str__(self):
        return self.name


class Graph:
    def __init__(self, edges=None, directed=False):
        self.vertices = {}
        self.directed = directed
        if edges:
            self.add_edges(edges)

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def add_edges(self, edges):
        for from_vertex, to_vertices in edges:
            self.add_vertex(from_vertex)
            for to_vertex in to_vertices:
                self.add_vertex(to_vertex)
                self.vertices[from_vertex].add_neighbor(
                    self.vertices[to_vertex])
                if not self.directed:
                    self.vertices[to_vertex].add_neighbor(
                        self.vertices[from_vertex])

    def get_vertex(self, name):
        return self.vertices.get(name)

    def reset_visits(self):
        for vertex in self.vertices.values():
            vertex.visited = False


class DepthFirstSearch:
    def __init__(self):
        self.stack = deque()

    def dfs(self, vertex_list):
        for vertex in vertex_list:
            if not vertex.visited:
                vertex.visited = True
                self.dfs_helper(vertex)

    def dfs_helper(self, root_vertex):
        self.stack.append(root_vertex)
        root_vertex.visited = True

        while self.stack:
            actual_vertex = self.stack.pop()
            print(actual_vertex)

            for neighbor in actual_vertex.adjacency_list:
                if not neighbor.visited:
                    neighbor.visited = True
                    self.stack.append(neighbor)
