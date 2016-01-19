class Node(object):
 
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList(object):

    def __init__(self):
        self.head = None
       
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
