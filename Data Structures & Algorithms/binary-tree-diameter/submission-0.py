# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter_val = 0 
        def diameter(node):
            if not node:
                return 0
            left_h=diameter(node.left)
            right_h=diameter(node.right)
            self.diameter_val = max(self.diameter_val,left_h+right_h)
            return max(left_h,right_h)+1
        diameter(root)
        return self.diameter_val