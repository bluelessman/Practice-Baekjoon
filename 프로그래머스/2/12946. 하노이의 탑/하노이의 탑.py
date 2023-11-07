def hanoi(n,start,end,middle,answer):
    if n == 1:
        return answer.append([start,end])
    hanoi(n-1,start,middle,end,answer)
    answer.append([start,end])
    hanoi(n-1,middle,end,start,answer)

def solution(n):
    answer = []
    hanoi(n,1,3,2,answer)
    return answer