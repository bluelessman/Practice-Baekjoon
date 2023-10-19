while True:
    n = int(input())
    if n == -1:
        break
    numlist = []
    for i in range(1,n):
        if(n%i==0):
            numlist.append(i)
    if sum(numlist) == n:
        #print(f"{n} = {'+'.join(numlist)}")

        print(n,"=",end=' ')
        print(*numlist, sep=' + ')
    else:
        print(f"{n} is NOT perfect.")