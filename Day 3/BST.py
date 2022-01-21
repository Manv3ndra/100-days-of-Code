class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, val):
        if self.data == val:
            print(str(self.data) + " found in the tree")

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                print(str(self.data) + " not found in the tree")

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                print(str(self.data) + " not found in the tree")

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

elements = [17,1,56,23,44,8,34,12]
root = Node(elements[0])
for i in range(1,len(elements)):
    root.insert(elements[i])
root.search(20)
root.search(12)
print("Inorder Traversal of tree gives: ",root.inorderTraversal(root))
print("Preorder Traversal of tree gives: ",root.PreorderTraversal(root))
print("Postorder Traversal of tree gives: ",root.PostorderTraversal(root))
root.delete(12)
print("Inorder Traversal of tree gives: ",root.inorderTraversal(root))
print("Preorder Traversal of tree gives: ",root.PreorderTraversal(root))
print("Postorder Traversal of tree gives: ",root.PostorderTraversal(root))