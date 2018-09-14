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

        

if __name__ == '__main__':
    unittest.main() 