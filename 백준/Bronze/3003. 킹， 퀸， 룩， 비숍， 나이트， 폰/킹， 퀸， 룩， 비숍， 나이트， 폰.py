K = 1
Q = 1
R = 2
B = 2
N = 2
P = 8
default_set = [1,1,2,2,2,8]
white = list(map(int, input().split()))
for i in range(6):
    print(default_set[i]-white[i],end=" ")