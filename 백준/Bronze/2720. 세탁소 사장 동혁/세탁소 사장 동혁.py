N = int(input())
for i in range(N):
    C = int(input())
    Q = C//25
    D = (C%25)//10
    N = ((C%25)%10)//5
    P = C%5
    print(f"{Q} {D} {N} {P}")
    