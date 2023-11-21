a = input()
nlist = [0]*26
for i in a:
    nlist[ord(i)-97] += 1
for i in nlist:
    print(i,end=" ")