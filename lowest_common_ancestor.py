class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def lca(root, val_1, val_2):
    val_1_list = []
    val_2_list = []
    path_to_value(root, val_1, val_1_list)
    path_to_value(root, val_2, val_2_list)
    print(val_1_list)
    print(val_2_list)
    val_1_set = set(val_1_list)
    for item in val_2_list:
        if item in val_1_set:
            return item
   
def path_to_value(node, value, node_list):
    node_list.insert(0, node)
    if node.data > value:
        path_to_value(node.left, value, node_list)
    elif node.data < value:
        path_to_value(node.right, value, node_list)

def main():
    root = Node(0)
    root.left = Node(-10)
    root.left.left = Node(-20)
    root.left.right = Node(-5)
    root.left.left.right = Node(-15)
    root.right = Node(10)
    print lca(root, -15, -5)

main()
    

