total = int(input())
count = int(input())
real_total = 0
for i in range(0, count) : 
    price, stock = map(int,input().split())
    real_total += price * stock
if real_total == total : print("Yes")
else : print("No")