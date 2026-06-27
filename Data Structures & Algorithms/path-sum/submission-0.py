# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr = 0

        def backtrack(root, add_up):
            if not root:
                return False

            add_up += root.val
            if not root.left and not root.right:
                if add_up != targetSum:
                    return False
                else:
                    return True
            
            if backtrack(root.left, add_up):
                return True
            
            if backtrack(root.right, add_up):
                return True
            
            add_up -= root.val
            return False

        return backtrack(root, curr)