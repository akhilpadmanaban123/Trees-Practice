# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            return 1+self.minDepth(root.right)
        
        if root.right is None:
            return 1+self.minDepth(root.left)

        return min(self.minDepth(root.left),self.minDepth(root.right))+1
        

        '''
        queue=[]
        if root is None:
            return 0
        if root is not None:
            queue.append(root)
        depth=1
        while queue:
            s=len(queue)
            for i in range(s):
                cur=queue.pop(0)
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            depth+=1
        return depth

        '''
