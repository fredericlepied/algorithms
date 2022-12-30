import unittest

import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_(self):
        g = dijkstra.Graph(9)
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
        res = g.dijkstra(0)

        expected = [0, 4, 12, 19, 21, 11, 9, 8, 14]
        self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()

# test_dijkstra.py ends here
