N = int(input())
ans = N//5
N = N%5
while N != 0:
    if N%3 == 0:
        ans += N//3
        break
    elif ans == 0:
        ans = -1
        break
    else:
        ans -= 1
        N += 5
print(ans)