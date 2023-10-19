N = int(input())
count = 1
while 2*N>count*(count+1):
    count += 1
numcount = N - (count*(count-1))//2
if count % 2 == 0:
  print(f"{numcount}/{count-numcount+1}")
else:
  print(f"{count-numcount+1}/{numcount}")
