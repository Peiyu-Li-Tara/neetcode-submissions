class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def insert_helper(root, key, val):
            if not root:
                return TreeNode(key, val)
            if key < root.key:
                root.left = insert_helper(root.left, key, val)
            elif key > root.key:
                root.right = insert_helper(root.right, key, val)
            else:
                root.val = val
            return root
        self.root = insert_helper(self.root, key, val)
        print(self.getInorderKeys())
            

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr.left:
            curr = curr.left
        return curr.val if curr else -1


    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1
        while curr.right:
            curr = curr.right
        return curr.val if curr else -1


    def remove(self, key: int) -> None:
        def find_right_min(root):
            curr = root
            while curr.left:
                curr = curr.left
            return curr

        def remove_helper(root, key):
            if not root:
                return None
            if key < root.key:
                root.left = remove_helper(root.left, key)
            elif key > root.key:
                root.right = remove_helper(root.right, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                else:
                    right_min_node = find_right_min(root.right)
                    root.val = right_min_node.val
                    root.key = right_min_node.key
                    root.right = remove_helper(root.right, root.key)
            return root
        
        self.root = remove_helper(self.root, key)


    def getInorderKeys(self) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)
        
        dfs(self.root)
        return res
        

