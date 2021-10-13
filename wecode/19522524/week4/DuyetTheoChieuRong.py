import sys

#len_root=0

temp= -1

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

ans={}

def insert(root, key,len_root=0):

    if root is None:

        if ans.get(len_root) is None:
            ans[len_root] = [key]
        else:
            ans[len_root].append(key)
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key,len_root+1)
        else:
            root.left = insert(root.left, key,len_root+1)

    return root

root= None

while temp != 0:
    temp= sys.stdin.readline()
    if temp=='\n':
        continue
    temp = int(temp)
    if temp ==0:
        break
    root= insert(root,temp)



i=1
while ans.get(i) is not None:
    if len(ans[i]) >1:
        ans[i].sort()
    i+=1

for j in range(i):
    print(*ans[j],end=' ')