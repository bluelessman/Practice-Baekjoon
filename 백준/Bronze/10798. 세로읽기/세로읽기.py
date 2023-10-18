answer = []
for i in range(15):
    answer.append([])
for i in range(5):
    count = 0
    a = input()
    for j in a:
        answer[count].append(j)
        count += 1
for i in answer:
    for j in i:
        print(j, end="")