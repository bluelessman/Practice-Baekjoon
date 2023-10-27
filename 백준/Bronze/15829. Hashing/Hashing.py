L = int(input())
word = input()
r=31
M=1234567891
hash = 0
count = 0
for i in word:
  hash += ((ord(i)-96)*(r**count))
  count += 1
print(hash%M)