# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p,q):
            if not p and not q:
                return True 
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
        
        def dfs(tree,subtree):
            if not tree:
                return False
            if not subtree:
                return True 
            if sameTree(tree,subtree):
                return True
            return dfs(tree.left,subtree) or dfs(tree.right,subtree)
        return dfs(root,subRoot)