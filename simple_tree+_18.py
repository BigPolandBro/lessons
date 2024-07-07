class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.Level = 0
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root
	
    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            return
        NewChild.Parent = ParentNode
        NewChild.Level = ParentNode.Level + 1
        ParentNode.Children.append(NewChild)
  
    def DeleteNode(self, NodeToDelete):
        parent = NodeToDelete.Parent
        NodeToDelete.Parent = None
        NodeToDelete.Level = 0
        parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        def helper(Node):
            res = [Node]
            for ChildNode in Node.Children:
                res.extend(helper(ChildNode))
            return res
        return helper(self.Root)

    def FindNodesByValue(self, val):
        def helper(Node):
            res = []
            if Node.NodeValue == val:
                res.append(Node)
            for ChildNode in Node.Children:
                res.extend(helper(ChildNode))
            return res
        return helper(self.Root)
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        def helper(Node):
            res = 1
            for ChildNode in Node.Children:
                res += helper(ChildNode)
            return res
        return helper(self.Root)

    def LeafCount(self):
        def helper(Node):
            res = 0 
            if len(Node.Children) == 0:
                res = 1
            for ChildNode in Node.Children:
                res += helper(ChildNode)
            return res
        return helper(self.Root)
        
    def CalcLevels(self):
        def helper(Node):
            if Node.Parent is not None:
                Node.Level = Node.Parent.Level + 1
            else:
                Node.Level = 0
                
            for ChildNode in Node.Children:
                helper(ChildNode)
        helper(self.Root)
        
    def EvenTrees(self):
        if self.Count() & 1:
            return []
            
        edges = []
            
        def helper(Node):
            res = 1
            for ChildNode in Node.Children:
                subres = helper(ChildNode)
                res += subres
                if not subres & 1:
                    edges.append(Node)
                    edges.append(ChildNode)
            return res
        helper(self.Root)
        return edges


