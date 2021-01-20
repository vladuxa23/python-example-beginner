import time
    import math

def summa(lst):

    if lst == []:
        return 0
    return (lst[0] + summa(lst[1:]))

def count(lst):

    if lst == []:
        return 0
    return (1 + count(lst[1:]))

def check_collatz():

    def collatz(number):
        if number%2 == 0:
            return number//2
        elif number%2 == 1:
            return 3*number+1

    def check_input():

        i = None
        while i != int():
            try:
                i = int(input())
                return i
            except ValueError as err:
                print(err)

    i = check_input()
    start_time = time.perf_counter()

    while i > 1:
        i = collatz(i)
        print(i)
    print ("{:g} s".format(time.perf_counter() - start_time))

def check_fibonachchi():

    def fib(n,k):
        return (math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))))

    n, k = map(int, input().split())
    if k == 0:
        print('1')
    elif k > n:
        print('0')
    else:
        print(int(fib(n,k)))


