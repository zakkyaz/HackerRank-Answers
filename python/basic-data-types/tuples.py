#DISCLAIMER: Change language to Pypy 3. Does not work with Python 3.

if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split()]
    t = tuple(numbers)
    print(hash(t))
