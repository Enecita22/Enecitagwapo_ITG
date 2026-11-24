
# POSTORDER TRAVERSAL IN BINARY TREE
# Name: JESPER ENECITA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# PostOrder Traversal
# Left -> Right -> Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


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
print("       POSTORDER TRAVERSAL")
print("===================================")
print("Name: JESPER ENECITA")
print("Traversal: Left -> Right -> Root")
print("-----------------------------------")

print("PostOrder Output:")
postorder(root)

print("\n-----------------------------------")
print("       PROGRAM COMPLETED")
print("===================================")
