n = [0 for i in range(30)]
for i in range(28):
    x = int(input())
    n[x-1]=x
for i in range(30):
    if n[i] == 0:
        print(i+1)