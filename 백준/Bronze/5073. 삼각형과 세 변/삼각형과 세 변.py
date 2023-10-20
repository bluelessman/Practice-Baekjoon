while True:
    num=list(map(int,input().split()))
    if num[0] == 0:
      break
    elif sum(num)-max(num) <= max(num):
      print("Invalid")
    elif num[0]==num[1] or num[0]==num[2] or num[1]==num[2]:
      if num[0]==num[1] and num[1]==num[2]:
        print("Equilateral")
      else:
        print("Isosceles")
    else:
      print("Scalene")
    
    