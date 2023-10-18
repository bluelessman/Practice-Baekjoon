N = int(input())
for i in range(1,2*N):
    star = " "*abs(N-i)+"*"*(2*(N-abs(N-i))-1)
    print(star)