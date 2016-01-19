'''
returns the index of the target, or False if the target is not in the list
'''
def binary_search_iterative(lst, target):
    lower_bound = 0
    middle = len(lst) / 2
    upper_bound = len(lst)

    while lst[middle] != target and lower_bound - upper_bound != -1:
        if lst[middle] > target:
            upper_bound = middle
        if lst[middle] < target:
            lower_bound = middle
        middle = (upper_bound + lower_bound) / 2

    if lst[middle] == target:
        return middle
    return False

def binary_search_recursive(lst, target, offset):
    middle = len(lst) / 2

    if lst[middle] == target:
        return middle + offset    
    if len(lst) < 2:
	return False
    if lst[middle] > target:
        return binary_search_recursive(lst[:middle], target, offset)
    elif lst[middle] < target:
        return binary_search_recursive(lst[middle:], target, offset + middle)

def main():
    x = range(-1, 8)
    for i in range(-1, 10):
        print binary_search_iterative(x, i), binary_search_recursive(x, i, 0)

main()
