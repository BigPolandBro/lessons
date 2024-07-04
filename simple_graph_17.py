class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        vid = None
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                vid = i
                break
        self.vertex[vid] = Vertex(v)
	
    def RemoveVertex(self, v):
        self.vertex[v] = None 
        for u in range(self.max_vertex):
            self.m_adjacency[v][u] = 0
            self.m_adjacency[u][v] = 0
	
    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] != 0:
            return True
        return False
	
    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0



    	
