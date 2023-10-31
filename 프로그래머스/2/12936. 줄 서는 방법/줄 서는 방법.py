from math import factorial
def solution(n, k):
    answer = []
    nlist = [i for i in range(1,n+1)]
    k -= 1
    while True:
        a, k = divmod(k, factorial(len(nlist)-1))
        answer.append(nlist.pop(a))
        if not nlist:
            break
    return answer