# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        else:
            return 0


    '''
    if root is None:
            return 0
        queue=[]
        queue.append(root)
        depth=0
        while queue:
            s=len(queue)
            for i in range(s):
                cur=queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            depth+=1
        return depth
        
