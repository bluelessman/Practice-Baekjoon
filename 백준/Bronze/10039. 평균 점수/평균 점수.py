score = []
for i in range(5):
    n = int(input())
    if n <40:
        n = 40
    score.append(n)
print(sum(score)//5)