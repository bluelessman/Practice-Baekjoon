h,m=map(int,input().split())
cooktime=int(input())
cookm = (m+cooktime)%60
cookh = h+(m+cooktime)//60
if cooktime+m < 60 : print(cookh, cookm)
else :
    if cookh<24 : print(cookh, cookm)
    else : print(cookh-24, cookm)