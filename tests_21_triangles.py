import unittest
import itertools
import random

class TestSimpleGraph(unittest.TestCase):
    
    def setUp(self):
        self.graph = SimpleGraph(10)
        for i in range(10):
            self.graph.AddVertex(100+i)
            
        edges = [0, 1, 0, 2, 0, 3, 1, 3, 1, 5, 2, 4, 2, 5, 3, 4, 5, 7, 6, 8, 6, 9, 8, 9]
        
        for i in range(0, len(edges), 2):
            #print(edges[i], edges[i+1])
            self.graph.AddEdge(edges[i], edges[i+1])
    
    def test_weak_vertices_setup(self):
        self.assertEqual(self.graph.WeakVertices(), self.graph.IndexListToVertexList([2, 4, 5, 7]))
        
    def test_weak_vertices_no_edges(self):
        graph = SimpleGraph(10)
        for i in range(5):
            graph.AddVertex(i + 100)
        self.assertEqual(graph.WeakVertices(), graph.IndexListToVertexList([0, 1, 2, 3, 4]))
        
    def test_tree_structure(self):
        graph = SimpleGraph(4)
        for i in range(4):
             graph.AddVertex(i + 100)
        graph.m_adjacency = [
            [0, 1, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ]
        self.assertEqual(graph.WeakVertices(), graph.IndexListToVertexList([0, 1, 2, 3]))
        
    def test_complex_structure(self):
        graph = SimpleGraph(6)
        for i in range(6):
            graph.AddVertex(i + 100)
        graph.m_adjacency = [
            [0, 1, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0]
        ]
        self.assertEqual(graph.WeakVertices(), graph.IndexListToVertexList([4, 5]))

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
