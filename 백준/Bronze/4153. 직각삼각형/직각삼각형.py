while True:
  ans = 0
  tri = list(map(int,input().split()))
  if tri[0] == 0:
    break
  else:
    for i in tri:
      ans += i**2
    ans -= (max(tri)**2)*2
    if ans == 0:
      print("right")
    else:
      print("wrong")