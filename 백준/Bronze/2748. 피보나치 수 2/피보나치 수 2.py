f = [0,1,1]+[-1]*90
def fib(n):
    if f[n] == -1:
        f[n] = fib(n-1)+fib(n-2)
    return f[n]
n = int(input())
print(fib(n))