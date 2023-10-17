n = int(input())
score = list(map(int,input().split()))
M = max(score)
for i in range(n):
    score[i] = score[i]*100/M
print(sum(score)/n)