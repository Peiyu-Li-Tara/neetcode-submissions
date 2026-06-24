# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Idea: a tree is height-balanced if all the nodes in this tree is height_balanced
        # We need to traverse through each node of this tree and see if the node is height-balanced
        # We can use recursion to split the problem into sub-problems until we hit the base case
        # For each subproblem, instead of return boolean, we need to return the height of the sub-tree as well

        def dfs(root: Optional[TreeNode]):
            if not root:
                return (True, 0)
            
            l_isBalanced, l_height = dfs(root.left)
            r_isBalanced, r_height = dfs(root.right)

            return (
                l_isBalanced and r_isBalanced and abs(l_height - r_height) <= 1,
                max(l_height, r_height) + 1
                )
        
        return dfs(root)[0]



            
