import unittest
from graph import Vertex
class VertexTests(unittest.TestCase):
    def setUp(self):
        self.vertex = Vertex(5)  # Instantiate your graph
    
    def test_instance(self):
        self.assertEqual(self.vertex.label, '5')
        self.assertEqual(self.vertex.component, -1)

if __name__ == '__main__':
    unittest.main() 