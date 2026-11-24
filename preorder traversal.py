
# PREORDER TRAVERSAL IN BINARY TREE
# Name: JESPER ENECITA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# PreOrder Traversal
# Root -> Left -> Right
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


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
print("       PREORDER TRAVERSAL")
print("===================================")
print("Name: JESPER ENECITA")
print("Traversal: Root -> Left -> Right")
print("-----------------------------------")

print("PreOrder Output:")
preorder(root)

print("\n-----------------------------------")
print("       PROGRAM COMPLETED")
print("===================================")
