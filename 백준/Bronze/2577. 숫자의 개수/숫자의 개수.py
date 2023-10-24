N = 1
for i in range(3):
    N *= int(input())
for i in range(10):
    print(str(N).count(str(i)))