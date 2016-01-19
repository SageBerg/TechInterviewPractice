from random import randint

def quick_sort_recursive(lst):
    if is_sorted(lst):
	return lst
    pivot = lst[0]
    lower = []
    pivots = []
    higher = []
    for item in lst:
        if item < pivot:
            lower.append(item)
        elif item == pivot:
            pivots.append(item)
        else:
            higher.append(item)
    return quick_sort_recursive(lower) + \
           pivots + \
           quick_sort_recursive(higher)

def is_sorted(lst):
    if len(lst) < 2:
        return True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def main():
    x = []
    for i in range(10):
	x.append(randint(1, 100))
    print x
    print quick_sort_recursive(x)

main()
