# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursively
        # res = []

        # def traverse(root: Optional[TreeNode]):
        #     if root is None:
        #         return 
        #     traverse(root.left)
        #     res.append(root.val)
        #     traverse(root.right)

        # traverse(root)
        # return res

        # iteratively
        stack, res = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right     
        
        return res

        
        