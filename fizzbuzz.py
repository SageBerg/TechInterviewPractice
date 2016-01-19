for i in range(1, 100):
    if not i % 3 and not i % 5:
        print i, "fizzbuzz"
    elif not i % 3:
        print i, "fizz"
    elif not i % 5:
        print i, "buzz"
