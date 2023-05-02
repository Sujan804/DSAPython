# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        inOrderList = []
        def inOrderTraversal(temp: Optional[TreeNode]):
            if temp is None:
                return
            if temp.left:
                inOrderTraversal(temp.left)
            inOrderList.append(temp.val)
            if temp.right:
                inOrderTraversal(temp.right)
        inOrderTraversal(root)
        print(inOrderList)
        for i in range(len(inOrderList)-1):
            if inOrderList[i] >= inOrderList[i+1]:
                return False
        return True
