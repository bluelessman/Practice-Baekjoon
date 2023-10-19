N = int(input())
numlist = list(map(int,input().split()))
answer = 0
for i in numlist:
    if i == 1:
      continue
    rooti = int(i**0.5)
    isdecimal = True
    for j in range(2,rooti+1):
        if i%j == 0:
            isdecimal = False
            break
    if isdecimal:
        answer += 1
print(answer)