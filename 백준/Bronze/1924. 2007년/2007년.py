x,y=map(int,input().split())
year = [0,1,4,4,0,2,5,0,3,6,1,4,6]
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
print(day[(year[x]+y-1)%7])