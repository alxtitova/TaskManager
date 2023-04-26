from collections import defaultdict

class Graph:
    def __init__(self, N):
        self.graph = defaultdict(list)
        self.nodes = N

    def add_edge(self, v, u):
        self.graph[v].append(u)

    def topological_sort_recursive(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_recursive(i, visited, stack)

        stack.append(v)

    def topological_sort(self):
        visited = [False for i in range(self.nodes)]
        stack = []

        for i in range(self.nodes):
            if not visited[i]:
                self.topological_sort_recursive(i, visited, stack)

        return stack

    def check_for_cycles(self):
        s = self.topological_sort()[::-1]

        for i in range(self.nodes):
            for j in self.graph[i]:
                left = 0 if i not in s else s.index(i)
                right = 0 if j not in s else s.index(j)

                if left > right:
                    return True

        return False