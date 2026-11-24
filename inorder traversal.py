
# INORDER TRAVERSAL IN BINARY TREE
# Name: JESPER ENECITA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# InOrder Traversal
# Left -> Root -> Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Create Binary Tree
root = Node("J")
root.left = Node("E")
root.right = Node("S")

root.left.left = Node("P")
root.left.right = Node("E")

root.right.left = Node("R")
root.right.right = Node("E")

root.left.left.left = Node("N")
root.left.left.right = Node("I")

root.left.right.left = Node("C")
root.left.right.right = Node("T")

root.right.left.left = Node("A")


# Main Program
print("===================================")
print("        INORDER TRAVERSAL")
print("===================================")
print("Name: JESPER ENECITA")
print("Traversal: Left -> Root -> Right")
print("-----------------------------------")

print("InOrder Output:")
inorder(root)

print("\n-----------------------------------")
print("       PROGRAM COMPLETED")
print("===================================")
