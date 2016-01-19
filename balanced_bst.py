class Node(object):

    def __init__(self):
        self.left = None
        self.right = None

def is_balanced(root):
    if check_height(root) == -1:
        return False
    return True

def check_height(node):
    if node == None:
        return 0
    left_height = check_height(node.left)
    if left_height == -1:
	return -1
    right_height = check_height(node.right)
    if right_height == -1:
	return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

def main():
    root = Node()
    root.left = Node()
    root.left.left = Node()
    root.left.left.right = Node()
    root.right = Node()
    print is_balanced(root)

main()
    

