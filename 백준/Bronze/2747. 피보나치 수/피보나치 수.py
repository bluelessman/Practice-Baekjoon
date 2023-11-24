fiblist = [0,1]
def fib(n):
    if len(fiblist) > n:
        return fiblist[n]
    else:
        fiblist.append(fib(n-1)+fib(n-2))
        return fiblist[n]
n = int(input())
print(fib(n))