a = input()
b = [-1 for i in range(26)]
count = 0
for i in a :
    if b[ord(i)-97] == -1 : b[ord(i)-97] = count
    count += 1
for i in b :
    print(i, end=" ")