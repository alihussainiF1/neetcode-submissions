# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append('#')
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            print(data)
            return None
        data=data.split(',')
        q=collections.deque()
        root=TreeNode(int(data[0]))
        q.append(root)
        i=1
        while q:
            node=q.popleft()
            if data[i]!='#':
                node.left=TreeNode(int(data[i]))
                q.append(node.left)
            i+=1
            if data[i]!='#':
                node.right=TreeNode(int(data[i]))
                q.append(node.right)
            i+=1
        return root
                