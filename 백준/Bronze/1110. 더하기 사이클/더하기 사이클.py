N = int(input())
first = N
count = 0
while True:
    count += 1
    temp = (N%10)*10 + (N//10 + N%10)%10
    if first == temp:
        print(count)
        break
    else:
        N = temp