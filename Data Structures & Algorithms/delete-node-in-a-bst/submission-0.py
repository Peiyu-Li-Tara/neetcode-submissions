# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findMinNode(root) -> Optional[TreeNode]:
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                minNode = findMinNode(root.right)
                root.val = minNode.val
                print(root.val)
                root.right = self.deleteNode(root.right, minNode.val)
        print(root.val)
        return root