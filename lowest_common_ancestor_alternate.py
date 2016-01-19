class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

#assumes a binary search tree
def lca(root, val_1, val_2):
    node = root
    paths_diverged = False
    while not paths_diverged:
        if val_1 < node.data and val_2 < node.data:
            node = node.left
        elif val_1 > node.data and val_2 > node.data:
            node = node.right
     	else:
            return node
    
def main():
    root = Node(0)
    root.left = Node(-10)
    root.left.left = Node(-20)
    root.left.right = Node(-5)
    root.left.left.right = Node(-15)
    root.right = Node(10)
    print lca(root, -20, -15)

main()
    

