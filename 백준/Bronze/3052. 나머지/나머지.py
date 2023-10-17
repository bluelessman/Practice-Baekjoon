numlist = [0 for i in range(42)]
count = 0
for i in range(10):
    n=int(input())%42
    if numlist[n]==0:
        count+=1
        numlist[n]=1
print(count)
    