import sys
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.left, key)
    return root
# print(*a)
def countt(root):
    if root == None:
        return 0
    else:
        if root.left == None and root.right == None:
            return 1
        else:
            return countt(root.left) + countt(root.right)
root = None
while True:
    k = int(sys.stdin.readline()[:-1])
    if k != 0:
        root = insert(root, k)
    else:
        print(countt(root))
        break

# def print_tree(root):
#     if root == None:
#         return
#     print(root.val)
#     print_tree(root.right)
#     print_tree(root.left)

# print(b[0])