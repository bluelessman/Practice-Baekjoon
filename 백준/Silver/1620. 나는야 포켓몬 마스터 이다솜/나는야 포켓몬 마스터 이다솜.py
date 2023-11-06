import sys
n,m = map(int,sys.stdin.readline().split())
poketmon_list = [0]
poketmon_dic = dict()
for i in range(n):
    poketmon = sys.stdin.readline().rstrip()
    poketmon_list.append(poketmon)
    poketmon_dic[poketmon] = i+1
for i in range(m):
    order = sys.stdin.readline().rstrip()
    if order.isdigit():
        print(poketmon_list[int(order)])
    else:
        print(poketmon_dic[order])
    