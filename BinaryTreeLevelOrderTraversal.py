# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue,result=[],[]
        if root is not None:
            queue.append(root)      # Queue appended with root

        while queue:        #Until queue becomes emtpy list []
            level=[]        # Each levels
            s=len(queue) # Length of each level
            for i in range(s):
                node=queue.pop(0)  # Node is first element
                level.append(node.val)
                if node.left is not None:       # Additing left node is its not empty
                    queue.append(node.left)
                if node.right is not None:      #Adding right node, if its not empty
                    queue.append(node.right)
            result.append(level)        # The main answer where each level values are stored

        return result
