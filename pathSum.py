# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum-=root.val
        if root.left is None and root.right is None and targetSum==0:
            return True
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right,targetSum)
    
    
    
#---------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        queue=[(root,root.val)]
        while queue:
            node, val=queue.pop(0)
            if node.left is not None:
                queue.append((node.left, val+node.left.val))
            if node.right is not None:
                queue.append((node.right, val+node.right.val))
            if node.left is None and node.right is None:
                if val==targetSum:
                    return True
                else:
                    continue
        return False
