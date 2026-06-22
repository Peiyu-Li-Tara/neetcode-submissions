# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return (True, 0)
            
            left, right = dfs(root.left), dfs(root.right)

            # Three conditions need to be met for balanced single node:
            # 1. If the left tree is balanced
            # 2. If the right tree is balanced
            # 3. If the height difference of the left tree and right tree is less than or equal to 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return (balanced, 1 + max(left[1], right[1]))
        
        return dfs(root)[0]
