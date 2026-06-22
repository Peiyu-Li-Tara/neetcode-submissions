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

        while len(queue) > 0:
            curr_len = len(queue)
            for _ in range(curr_len):
                curr = queue.popleft()
                curr_len -= 1
                if curr_len == 0:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return res

