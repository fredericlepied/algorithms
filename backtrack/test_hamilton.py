import unittest

import hamilton


class TestHamilton(unittest.TestCase):
    def test_hamilton(self):
        # consider a complete graph having 4 vertices
        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

        # total number of nodes in the graph (labelled from 0 to 3)
        n = 4

        # build a graph from the given edges
        graph = hamilton.Graph(edges, n)

        solutions = hamilton.findHamiltonianPaths(graph, n)
        self.assertEqual(len(solutions), 24)


if __name__ == "__main__":
    unittest.main()

# test_hamilton.py ends here
