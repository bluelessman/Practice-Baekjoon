fibList = [[1,0],[0,1]]
def fib(n):
    if len(fibList)<=n:
        temp = fib(n-1)+fib(n-2)
        fibList.append([temp[0]+temp[2],temp[1]+temp[3]])
    return fibList[n]
n = int(input())
for i in range(n):
    m = int(input())
    ans = fib(m)
    print(ans[0],ans[1])