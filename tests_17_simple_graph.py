import unittest
import itertools
import random

class TestSimpleGraph(unittest.TestCase):
    
    def setUp(self):
        self.graph = SimpleGraph(10)
        self.graph.AddVertex(200)
        self.graph.AddVertex(333)
        self.graph.AddVertex(666)
        self.graph.AddVertex(777)
        
        for u in range(4):
            for v in range(u + 1, 4):
                self.graph.AddEdge(u, v)
        
    def test_set_up(self):
        self.assertEqual(self.graph.max_vertex, 10)
        values = [200, 333, 666, 777]
        for v in range(4):
            self.assertEqual(self.graph.vertex[v].Value, values[v])
        
        for u in range(self.graph.max_vertex):
            for v in range(self.graph.max_vertex):
                target = 1 if u != v and u < 4 and v < 4 else 0
                self.assertEqual(self.graph.m_adjacency[u][v], target)
                self.assertEqual(self.graph.m_adjacency[v][u], target)
                target_bool = True if target == 1 else False 
                self.assertEqual(self.graph.IsEdge(u, v), target_bool)
                self.assertEqual(self.graph.IsEdge(v, u), target_bool)
                
    def test_add_edge(self):
        self.graph.AddVertex(404)
        u = 1
        v = 4
        self.assertEqual(self.graph.IsEdge(u, v), False)
        self.assertEqual(self.graph.IsEdge(v, u), False)
        self.graph.AddEdge(u, v)
        self.assertEqual(self.graph.IsEdge(u, v), True)
        self.assertEqual(self.graph.IsEdge(v, u), True)
        
    def test_delete_edge(self):
        u = 2
        v = 3
        self.assertEqual(self.graph.IsEdge(u, v), True)
        self.assertEqual(self.graph.IsEdge(v, u), True)
        self.graph.RemoveEdge(u, v)
        self.assertEqual(self.graph.IsEdge(u, v), False)
        self.assertEqual(self.graph.IsEdge(v, u), False)
    
    def test_add_vertex(self):
        v = 4
        for u in range(self.graph.max_vertex):
            self.assertEqual(self.graph.m_adjacency[u][v], 0)
            self.assertEqual(self.graph.m_adjacency[v][u], 0)
        self.assertEqual(self.graph.vertex[v], None)
        
        self.graph.AddVertex(404)
        
        self.assertEqual(self.graph.vertex[v].Value, 404)
        for u in range(self.graph.max_vertex):
            self.assertEqual(self.graph.m_adjacency[u][v], 0)
            self.assertEqual(self.graph.m_adjacency[v][u], 0)
            
    def test_remove_vertex(self):
        v = 2
        
        self.assertEqual(self.graph.vertex[v].Value, 666)
        self.graph.RemoveEdge(0, v)
        for u in range(self.graph.max_vertex):
            target_bool = True if u < 4 and u != 0 and u != v else False
            self.assertEqual(self.graph.IsEdge(u, v), target_bool)
            self.assertEqual(self.graph.IsEdge(v, u), target_bool)
        
        self.graph.RemoveVertex(v)
        
        self.assertEqual(self.graph.vertex[v], None)
        for u in range(self.graph.max_vertex):
            self.assertEqual(self.graph.IsEdge(u, v), False)
            self.assertEqual(self.graph.IsEdge(v, u), False)
            
        self.graph.AddVertex(667)
        self.assertEqual(self.graph.vertex[v].Value, 667)

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
