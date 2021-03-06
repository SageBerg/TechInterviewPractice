from linked_list import *

def reverse(node):
    print_list(node)
    prev = None
    curr = node
    next = node.next
    
    while next != None:
        curr.next = prev
        prev = curr
        curr = next
        next = curr.next

    curr.next = prev
    print_list(curr)

def reverse_recursive(prev, curr, next):
    curr.next = prev
    if next != None:
        reverse_recursive(curr, next, next.next)
    else:
        print_list(curr)

def print_list(node):
    while node != None:
        print(node)
        node = node.next
    
def main():
    ll = LinkedList()
    for i in range(10):
        ll.push(i)
    print_list(ll.head)
    reverse_recursive(None, ll.head, ll.head.next)

main()
        

