def solution(n, results):
    total = [['????' for i in range(n)] for j in range(n)]
    answer = 0
    for i in range(n):
        total[i][i] = 'self'
    for result in results:
        total[result[0]-1][result[1]-1] = 'wins'
        total[result[1]-1][result[0]-1] = 'loses'
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'wins' and total[k][j] == 'wins':
                    total[i][j] = 'wins'
                elif total[i][k] == 'loses' and total[k][j] == 'loses':
                    total[i][j] = 'loses'
    for result in total:
        if result.count('????') == 0:
            answer += 1
    return answer