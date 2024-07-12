class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() <= 0:
            return None
        val = self.stack[self.size()-1]
        self.stack.pop()
        return val

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() <= 0:
            return None
        return self.stack[self.size()-1]

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
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
        return self.m_adjacency[v1][v2] != 0
	
    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        
    def VertexToIndex(self, vertex):
        for i in range(self.max_vertex):
            if self.vertex[i] == vertex:
                return i
                
    def VertexListToIndexList(self, vertex_list):
        index_list = []
        for vertex in vertex_list:
            index_list.append(self.VertexToIndex(vertex))
        return index_list
            
    def IndexToVertex(self, index):
        return self.vertex[index]
        
    def IndexListToVertexList(self, index_list):
        vertex_list = []
        for index in index_list:
            vertex_list.append(self.IndexToVertex(index))
        return vertex_list
        
    def DepthFirstSearch(self, VFrom, VTo):
        if VFrom == VTo:
            return self.IndexListToVertexList([VFrom])
            
        stack = Stack()
        x = VFrom
        next_found = True
        next_vertex = [0 for i in range(self.max_vertex)]
        for i in range(self.max_vertex):
            self.vertex[i].Hit = False
        
        while next_found:
            if not self.vertex[x].Hit:
                stack.push(x)
                self.vertex[x].Hit = True
                if self.IsEdge(x, VTo):
                    self.vertex[VTo].Hit = True
                    stack.push(VTo)
                    return self.IndexListToVertexList(stack.stack)

            next_found = False
            while next_vertex[x] < self.max_vertex and not next_found:
                y = next_vertex[x]
                next_vertex[x] += 1
                if self.IsEdge(x, y) and not self.vertex[y].Hit:
                    x = y
                    next_found = True

            if not next_found and stack.size() > 1:
                stack.pop()
                x = stack.peek()
                next_found = True
                
        return []



