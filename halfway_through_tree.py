from tree import Node

def get_median(lst):
    mid = len(lst) / 2
    if len(lst) % 2 == 0:
        return (float(lst[mid]) + float(lst[mid - 1])) / 2
    else:
        return lst[mid]

def bst_to_inorder_list(node, lst):
    if node == None:
        return lst
    bst_to_inorder_list(node.left, lst)
    lst.append(node.data)
    bst_to_inorder_list(node.right, lst)
    return lst

def get_tree_median(node):
    return get_median(bst_to_inorder_list(node, []))

def main():
    root = Node(0)
    root.left = Node(-10)
    root.left.left = Node(-20)
    root.left.right = Node(-5)
    root.right = Node(10)
    root.right.right = Node(20)
    print get_tree_median(root)

if __name__ == "__main__":
    main()
