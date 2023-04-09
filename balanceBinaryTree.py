# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        lefttt=self.heightCalc(root.left)
        rightt=self.heightCalc(root.right)
        if abs(rightt-lefttt)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True 
        return False
    
    def heightCalc(self, roott):
        if roott is None:
            return 0
        return max(self.heightCalc(roott.left),self.heightCalc(roott.right))+1
