from tree import Node
from Queue import Queue

def bfs(node, target):
    q = Queue()
    q.put(node) 
   
    while q:
        popped = q.get()
        if popped.data == target:
            return popped
        print popped
        if popped.left:
            q.put(popped.left)
        if popped.right:
            q.put(popped.right)

def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    for i in range(7):
        print bfs(root, i), "\n"

main()
