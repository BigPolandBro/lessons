class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False
    
    @staticmethod
    def with_parameters(node, node_has_key, to_left):
        instance = BSTFind()
        instance.Node = node
        instance.NodeHasKey = node_has_key
        instance.ToLeft = to_left
        return instance

class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        def helper(node, key):
            if node.NodeKey == key:
                return BSTFind.with_parameters(node, True, False)
            
            to_left = key < node.NodeKey
            next_node = node.LeftChild if to_left else node.RightChild
            
            if next_node is not None:
                return helper(next_node, key)
            return BSTFind.with_parameters(node, False, to_left)
                
        if self.Root is None:
            return BSTFind()
        return helper(self.Root, key)

    def AddKeyValue(self, key, val):
        find_node = self.FindNodeByKey(key)
        if find_node.NodeHasKey:
            return False
        
        node = find_node.Node
        new_node = BSTNode(key, val, node)
        if node is None:
            self.Root = new_node
        elif find_node.ToLeft:
            node.LeftChild = new_node
        else:
            node.RightChild = new_node
        return True
            
    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None
            
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
        return node
	
    def DeleteNodeByKey(self, key):
        find_node = self.FindNodeByKey(key)
        if not find_node.NodeHasKey:
            return False

        node = find_node.Node 
        if node.LeftChild is not None and node.RightChild is not None:
            next_node = self.FinMinMax(node.RightChild, False)
            node.NodeKey, node.NodeValue = next_node.NodeKey, next_node.NodeValue
            node = next_node
            
        child = node.LeftChild if node.LeftChild is not None else node.RightChild
        parent = node.Parent
        
        if parent is not None:
            if parent.LeftChild == node:
                parent.LeftChild = child
            else:
                parent.RightChild = child
        else:
            self.Root = child
            
        if child is not None:
            child.Parent = parent
            
        return True

    def Count(self):
        def helper(node):
            if node is None:
                return 0
            return 1 + helper(node.LeftChild) + helper(node.RightChild)
        return helper(self.Root)

