class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None

    def GenerateTree(self, a):
        sa = sorted(a)
        
        def helper(lb, rb, lvl):
            if lb > rb:
                return None
                
            md = (lb + rb) // 2
            node = BSTNode(sa[md], None)
            node.Level = lvl
            
            left = helper(lb, md - 1, lvl + 1)
            right = helper(md + 1, rb, lvl + 1)
            if left:
                node.LeftChild = left 
                left.Parent = node
            if right:
                node.RightChild = right 
                right.Parent = node
                
            return node

        self.Root = helper(0, len(a) - 1, 0)

    def IsBalanced(self, root_node):
        class HelperAns:

            def __init__(self, depth, is_balanced):
                self.Depth = depth 
                self.IsBalanced = is_balanced
                
        def helper(node):
            if node is None:
                return HelperAns(-1, True)
            leftAns = helper(node.LeftChild)
            rightAns = helper(node.RightChild)
            depth_left = leftAns.Depth
            depth_right = rightAns.Depth
            depth = max(depth_left, depth_right) + 1
            if not leftAns.IsBalanced or not rightAns.IsBalanced or abs(depth_left - depth_right) > 1:
                return HelperAns(depth, False)
            return HelperAns(depth, True)
        return helper(root_node).IsBalanced
        
    def IsSearch(self, root_node):
        if root_node is None:
            return True
        
        left = root_node.LeftChild
        right = root_node.RightChild
        if left and left.NodeKey >= root_node.NodeKey:
            return False
            
        if right and right.NodeKey < root_node.NodeKey:
            return False
            
        return self.IsSearch(left) and self.IsSearch(right)
        
    def TraverseTree(self):
        a = []
        def helper(node):
            if node is None:
                return
            a.append([node.Level, node.NodeKey])
            
            helper(node.LeftChild)
            helper(node.RightChild)
        
        helper(self.Root)
        a = sorted(a)
        return a

