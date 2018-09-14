import unittest
from graph import Graph
from graph import Vertex
class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()  # Instantiate your graph

    
    def test_add_vertex(self):
        vert0 = Vertex(0)
        vert1 = Vertex(1)
        self.graph.add_vertex(vert0)
        self.graph.add_vertex(vert1)
        
        self.assertDictEqual(self.graph.vertices, {
            vert0: set(),
            vert1: set()
        })

    def test_add_edge(self):
        vert0 = Vertex(0)
        vert1 = Vertex(1)
        # Bi-directional test
        self.graph.add_vertex(vert0)
        self.graph.add_vertex(vert1)
        self.graph.add_edge(vert0, vert1)

        self.assertDictEqual(self.graph.vertices, {
            vert0: {vert1},
            vert1: {vert0}
        })
        # Directional test
        vert2 = Vertex(2)
        vert3 = Vertex(3)

        self.graph.add_vertex(vert2)
        self.graph.add_vertex(vert3)
        self.graph.add_edge(vert2, vert3, False)
        self.assertDictEqual(self.graph.vertices, {
            vert0: {vert1},
            vert1: {vert0},
            vert2: {vert3},
            vert3: set()
        })

    def test_dfs(self):
        vert0 = Vertex(0)
        vert1 = Vertex(1)
        vert2 = Vertex(2)
        vert3 = Vertex(3)
        vert4 = Vertex(4)
        vert5 = Vertex(5)
        self.graph.add_vertex(vert0)
        self.graph.add_vertex(vert1)
        self.graph.add_vertex(vert2)
        self.graph.add_vertex(vert3)
        self.graph.add_vertex(vert4)
        self.graph.add_vertex(vert5)

        self.graph.add_edge(vert0, vert1)
        self.graph.add_edge(vert0, vert4)
        self.graph.add_edge(vert0, vert2)
        self.graph.add_edge(vert1, vert3)
        self.graph.add_edge(vert5, vert4)
        self.graph.add_edge(vert5, vert2)

        print(self.graph.dfs(vert5, vert1))
        # Does not reach Vertex 3 when 1 is found, where 1 is the target vertex
        self.assertLess(len(self.graph.dfs(vert5, vert1)), 6)
        
        

if __name__ == '__main__':
    unittest.main() 