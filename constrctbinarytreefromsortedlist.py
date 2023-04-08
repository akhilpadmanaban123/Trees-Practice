# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.binaryHelper(nums,0,len(nums))

    def binaryHelper(self, nums, start, end):
        if start>=end: return None
        mid=(start+end)//2
        return TreeNode(
            val=nums[(start+end)//2],
            left=self.binaryHelper(nums,start,mid),
            right=self.binaryHelper(nums,mid+1,end)
        )
        
