# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(node):
            if not node:
                return (0,True)
            left_h,left_balance = balanced(node.left)
            right_h,right_balance = balanced(node.right)
            current_balance = left_balance and right_balance and abs(left_h-right_h)<=1

            return (max(left_h,right_h)+1,current_balance)
        
        _,is_balanced = balanced(root)

        return is_balanced