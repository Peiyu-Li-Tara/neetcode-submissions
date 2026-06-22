# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # For each level, we traverse from left to right
        # We peek from right, so the last value we seen in the current level is visible
        queue = deque()
        res = []
        if root:
            queue.append(root)

        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                curr = queue.popleft()
                level_len -= 1
                if level_len == 0:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return res

