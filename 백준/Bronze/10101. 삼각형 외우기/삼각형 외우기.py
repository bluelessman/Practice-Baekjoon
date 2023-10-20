trilist = []
for i in range(3):
    trilist.append(int(input()))
if sum(trilist) != 180:
    print("Error")
elif trilist[0] == trilist[1] or trilist[1] == trilist[2] or trilist[0] == trilist[2]:
    if trilist[0] == trilist[1] and trilist[1] == trilist[2]:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    print("Scalene")
    