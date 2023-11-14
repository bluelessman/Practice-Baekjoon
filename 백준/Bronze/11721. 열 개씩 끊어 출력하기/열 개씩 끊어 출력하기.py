a = input()
count = 0
for i in a:
    print(i,end="")
    count += 1
    if count == 10:
        count = 0
        print()
    