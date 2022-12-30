import sys


class Graph:
    def __init__(self, num_vertices):
        self.num = num_vertices
        self.path = [0] * num_vertices

    def dijkstra(self, start):
        self.spt = []
        self.dist = [sys.maxsize] * self.num
        self.dist[start] = 0
        while len(self.spt) != self.num:
            idx = self.get_min()
            self.spt.append(idx)
            self.update_distances(idx)
        return self.dist

    def get_min(self):
        min = sys.maxsize
        res = -1
        for idx in range(self.num):
            if self.dist[idx] < min and idx not in self.spt:
                min = self.dist[idx]
                res = idx
        return res

    def update_distances(self, src):
        for dst in range(self.num):
            if self.graph[src][dst] > 0 and dst not in self.spt:
                dist = self.graph[src][dst] + self.dist[src]
                if dist < self.dist[dst]:
                    self.graph[src][dst] = dist
                    self.dist[dst] = self.graph[src][dst]
                    self.path[dst] = src

    def print_paths(self, start):
        for idx in range(self.num):
            if idx != start:
                path = [idx]
                cur = idx
                while cur != start:
                    path = [self.path[cur]] + path
                    cur = self.path[cur]
                print("->".join([str(x) for x in path]))


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0],
    ]
    print(g.dijkstra(0))
    g.print_paths(0)

# dijkstra.py ends here
