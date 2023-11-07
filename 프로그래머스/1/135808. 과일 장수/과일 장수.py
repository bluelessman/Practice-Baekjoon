def solution(k, m, score):
    answer = 0
    score = sorted(score,reverse=True)+[0]*m
    for i in range(0,len(score),m):
        if score[i]==0:
            break
        else:
            answer += m*score[i+m-1]
        
    return answer