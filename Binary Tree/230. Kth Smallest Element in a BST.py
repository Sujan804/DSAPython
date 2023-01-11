# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrderList = []

        def inOrderTraversal(temp):
            if not temp:
                return
            if temp.left:
                inOrderTraversal(temp.left)
            inOrderList.append(temp.val)
            if temp.right:
                inOrderTraversal(temp.right)
        inOrderTraversal(root)
        return inOrderList[k-1]