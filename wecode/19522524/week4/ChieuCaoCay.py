import sys
from collections import deque
l = deque()
while True:
    k = sys.stdin.readline()
    a = list(map(int, k[:len(k)-1].split()))
    if a[0] == 0:
        l.appendleft(a[1])
    elif a[0] == 1:
        l.append(a[1])
    elif a[0] == 2:
        try:
            index = l.index(a[1])
            l.insert(index+1,a[2])
            continue
        except:
            l.appendleft(a[1])
    else:
        break

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
root = None
s=set()
while len(l) != 0:
    x = l.popleft()
    if x not in s:
        s.add(x)
        root = insert(root, x)

def height_bi(root):
    if root == None:
        return 0
    else:
        return max(height_bi(root.left), height_bi(root.right)) + 1

print(height_bi(root))