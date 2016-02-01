from linked_list import Node, LinkedList

def insert(node, ll):
    prev = None
    curr = ll.head
    while curr != None:
        if node.data <= curr.data:
            if prev:
                prev.next = node
            else:
                ll.head = node
            node.next = curr
            return
        prev = curr
        curr = curr.next
    prev.next = node
    ll.tail = node

def main():
    ll = LinkedList()
    ll.push(5)
    ll.push(5)
    ll.push(3)
    ll.push(1)

    insert(Node(0), ll)
    insert(Node(2), ll)
    insert(Node(4), ll)
    insert(Node(5), ll)
    insert(Node(10), ll)

    node = ll.head
    while node != None:
        print node.data
        node = node.next

if __name__ == "__main__":
    main()
