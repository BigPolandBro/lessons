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
            
    def test_convert_index_vertex(self):
        vertex = self.graph.vertex[0]
        vertex2 = Vertex(100)
        # print(vertex.Value, vertex2.Value)
        # print(vertex.Hit, vertex2.Hit)
        # print(vertex == vertex2)
        self.assertEqual(self.graph.VertexToIndex(vertex), 0)
        self.assertEqual([0], self.graph.VertexListToIndexList([vertex]))
        self.assertEqual([vertex], self.graph.IndexListToVertexList([0]))
    
    def test_dfs(self):
        for a in [0, 1, 2, 3, 4, 5, 7]:
            for b in [6, 8, 9]:
                self.assertEqual(self.graph.DepthFirstSearch(a, b), self.graph.IndexListToVertexList([]))
        
        for a in range(0, 10):
            self.assertEqual(self.graph.DepthFirstSearch(a, a), self.graph.IndexListToVertexList([a]))
            
        for a in range(0, 10):
            for b in range(0, 10):
                if self.graph.IsEdge(a, b):
                    #print(a, b, self.graph.IsEdge(a, b))
                    self.assertEqual(self.graph.DepthFirstSearch(a, b), self.graph.IndexListToVertexList([a, b]))
                    
        for a in [6, 8, 9]:
            for b in [6, 8, 9]:
                if a == b:
                    continue
                self.assertEqual(self.graph.DepthFirstSearch(a, b), self.graph.IndexListToVertexList([a, b]))
                    
        self.assertEqual(self.graph.DepthFirstSearch(0, 4), self.graph.IndexListToVertexList([0, 1, 3, 4]))
        self.assertEqual(self.graph.DepthFirstSearch(2, 7), self.graph.IndexListToVertexList([2, 0, 1, 5, 7]))
        self.assertEqual(self.graph.DepthFirstSearch(7, 3), self.graph.IndexListToVertexList([7, 5, 1, 3]))
        self.assertEqual(self.graph.DepthFirstSearch(7, 4), self.graph.IndexListToVertexList([7, 5, 1, 0, 2, 4]))
        self.assertEqual(self.graph.DepthFirstSearch(0, 5), self.graph.IndexListToVertexList([0, 1, 5]))
        self.assertEqual(self.graph.DepthFirstSearch(0, 7), self.graph.IndexListToVertexList([0, 1, 3, 4, 2, 5, 7]))
        
    
    # def setUp(self):
    #     self.graph = SimpleGraph(10)
    #     self.graph.AddVertex(200)
    #     self.graph.AddVertex(333)
    #     self.graph.AddVertex(666)
    #     self.graph.AddVertex(777)
        
    #     for u in range(4):
    #         for v in range(u + 1, 4):
    #             self.graph.AddEdge(u, v)
        
    # def test_set_up(self):
    #     self.assertEqual(self.graph.max_vertex, 10)
    #     values = [200, 333, 666, 777]
    #     for v in range(4):
    #         self.assertEqual(self.graph.vertex[v].Value, values[v])
        
    #     for u in range(self.graph.max_vertex):
    #         for v in range(self.graph.max_vertex):
    #             target = 1 if u != v and u < 4 and v < 4 else 0
    #             self.assertEqual(self.graph.m_adjacency[u][v], target)
    #             self.assertEqual(self.graph.m_adjacency[v][u], target)
    #             target_bool = True if target == 1 else False 
    #             self.assertEqual(self.graph.IsEdge(u, v), target_bool)
    #             self.assertEqual(self.graph.IsEdge(v, u), target_bool)
                
    # def test_add_edge(self):
    #     self.graph.AddVertex(404)
    #     u = 1
    #     v = 4
    #     self.assertEqual(self.graph.IsEdge(u, v), False)
    #     self.assertEqual(self.graph.IsEdge(v, u), False)
    #     self.graph.AddEdge(u, v)
    #     self.assertEqual(self.graph.IsEdge(u, v), True)
    #     self.assertEqual(self.graph.IsEdge(v, u), True)
        
    # def test_delete_edge(self):
    #     u = 2
    #     v = 3
    #     self.assertEqual(self.graph.IsEdge(u, v), True)
    #     self.assertEqual(self.graph.IsEdge(v, u), True)
    #     self.graph.RemoveEdge(u, v)
    #     self.assertEqual(self.graph.IsEdge(u, v), False)
    #     self.assertEqual(self.graph.IsEdge(v, u), False)
    
    # def test_add_vertex(self):
    #     v = 4
    #     for u in range(self.graph.max_vertex):
    #         self.assertEqual(self.graph.m_adjacency[u][v], 0)
    #         self.assertEqual(self.graph.m_adjacency[v][u], 0)
    #     self.assertEqual(self.graph.vertex[v], None)
        
    #     self.graph.AddVertex(404)
        
    #     self.assertEqual(self.graph.vertex[v].Value, 404)
    #     for u in range(self.graph.max_vertex):
    #         self.assertEqual(self.graph.m_adjacency[u][v], 0)
    #         self.assertEqual(self.graph.m_adjacency[v][u], 0)
            
    # def test_remove_vertex(self):
    #     v = 2
        
    #     self.assertEqual(self.graph.vertex[v].Value, 666)
    #     self.graph.RemoveEdge(0, v)
    #     for u in range(self.graph.max_vertex):
    #         target_bool = True if u < 4 and u != 0 and u != v else False
    #         self.assertEqual(self.graph.IsEdge(u, v), target_bool)
    #         self.assertEqual(self.graph.IsEdge(v, u), target_bool)
        
    #     self.graph.RemoveVertex(v)
        
    #     self.assertEqual(self.graph.vertex[v], None)
    #     for u in range(self.graph.max_vertex):
    #         self.assertEqual(self.graph.IsEdge(u, v), False)
    #         self.assertEqual(self.graph.IsEdge(v, u), False)
            
    #     self.graph.AddVertex(667)
    #     self.assertEqual(self.graph.vertex[v].Value, 667)

if __name__ == '__main__':
    print("BEFORE")
    unittest.main()
