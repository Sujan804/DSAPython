class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

      
        def dfs(node):
            if node is None:
                return False
            elif isIdentical(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)


        def isIdentical(node1, node2):
            if node1 is None or node2 is None:
                return node1 is None and node2 is None
            return (node1.val == node2.val and
                    isIdentical(node1.left, node2.left) and
                    isIdentical(node1.right, node2.right))
        return dfs(root)