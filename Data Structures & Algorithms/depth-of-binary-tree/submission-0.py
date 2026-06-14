# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        height_val = 0 
        if not root:
            return 0
        def height(node):
            if not node:
                return 0
            height_l=height(node.left)+1
            height_r=height(node.right)+1

            return max(height_l,height_r)
        height_val = height(root)
        return height_val
