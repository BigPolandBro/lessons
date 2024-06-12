class BSTNode:
	
    def __init__(self, key: int, val: str, parent: 'BSTNode'):
        self.NodeKey: int = key
        self.NodeValue: str = val
        self.Parent: 'BSTNode' = parent
        self.LeftChild: 'BSTNode' = None
        self.RightChild: 'BSTNode' = None


class BSTFind:

    def __init__(self):
        self.Node: 'BSTNode' = None
        self.NodeHasKey: bool = False
        self.ToLeft: bool = False
    
    @staticmethod
    def with_parameters(node: 'BSTNode', node_has_key: bool, to_left: bool) -> 'BSTFind':
        instance = BSTFind()
        instance.Node = node
        instance.NodeHasKey = node_has_key
        instance.ToLeft = to_left
        return instance

class BST:

    def __init__(self, node: 'BSTNode'):
        self.Root: 'BSTNode' = node

    def FindNodeByKey(self, key: int) -> 'BSTFind':
        def helper(node: 'BSTNode', key: int) -> 'BSTFind':
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

    def AddKeyValue(self, key: int, val: str) -> bool:
        find_node: 'BSTFind' = self.FindNodeByKey(key)
        if find_node.NodeHasKey:
            return False
        
        node: 'BSTNode' = find_node.Node
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
	
    def DeleteNodeByKey(self, key: int) -> bool:
        find_node: 'BSTFind' = self.FindNodeByKey(key)
        if not find_node.NodeHasKey:
            return False

        node: 'BSTNode' = find_node.Node 
        if node.LeftChild is not None and node.RightChild is not None:
            next_node = self.FinMinMax(node.RightChild, False)
            node.NodeKey, node.NodeValue = next_node.NodeKey, next_node.NodeValue
            node = next_node
            
        child: 'BSTNode' = node.LeftChild if node.LeftChild is not None else node.RightChild
        parent: 'BSTNode' = node.Parent
        
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

    def Count(self) -> int:
        def helper(node: 'BSTNode') -> int:
            if node is None:
                return 0
            return 1 + helper(node.LeftChild) + helper(node.RightChild)
        return helper(self.Root)
    
    def WideAllNodes(self) -> 'list[BSTNode]':
        if self.Root is None:
            return []
            
        queue = Queue()
        queue.enqueue(self.Root)
        res: 'list[BSTNode]' = []
        
        while queue.size() > 0:
            node = queue.dequeue()
            res.append(node)
            
            if node.LeftChild is not None:
                queue.enqueue(node.LeftChild)
            if node.RightChild is not None:
                queue.enqueue(node.RightChild)
                
        return res
    
    def DeepAllNodes(self, order: int) -> 'list[BSTNode]':
        def dfs(node: 'BSTNode', order: int) -> 'list[BSTNode]':
            if node is None:
                return []
            left_subtree = dfs(node.LeftChild, order)
            right_subtree = dfs(node.RightChild, order)
            if order == 0:
                res = left_subtree
                res.append(node)
                res.extend(right_subtree)
            elif order == 1:
                res = left_subtree
                res.extend(right_subtree)
                res.append(node)
            else:
                res = [node]
                res.extend(left_subtree)
                res.extend(right_subtree)
            return res
                
        return dfs(self.Root, order)
    
    def InvertTree(self) -> None:
        def invert(node: 'BSTNode') -> None:
            if node is None:
                return
            invert(node.LeftChild)
            invert(node.RightChild)
            node.LeftChild, node.RightChild = node.RightChild, node.LeftChild
        invert(self.Root)
    
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
        
class Queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()
        
    def change(self):
        while self.input.size() > 0:
            item = self.input.pop()
            self.output.push(item)

    def enqueue(self, item):
        self.input.push(item)

    def dequeue(self):
        if self.size() <= 0:
            return None
        if self.output.size() <= 0:
            self.change()
        return self.output.pop()

    def size(self):
        return self.input.size() + self.output.size()            
            
            
