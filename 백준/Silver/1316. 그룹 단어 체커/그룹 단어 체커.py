a = int(input())
answer = 0
for i in range(a):
    count = 0
    dic = {}
    isTrue = True
    string = input()
    for i in string:
        if i in dic and count-1 != dic[i]:
                isTrue = False
                break
        else :
            dic[i] = count
        count += 1
    if isTrue:
        answer += 1
print(answer)    
        