def solution(money):
    # for i in range(len(money)):
    #     m = i
    #     current = i
    #     for j in range(i,len(money)):
    #         if j-current > 1 and j-i!=len(money)-1:
    #             m += j
    #     if m > answer:
    #         answer = m
    l = [0]*len(money)
    l[0]= money[0]
    l[1]=l[0]
        
    for i in range(2,len(money)-1):
        l[i] = max(l[i-2]+money[i],l[i-1])   
        
    l2 = [0]*len(money)
    l2[1] = money[1]
    
    for i in range(2,len(money)):
        l2[i] = max(l2[i-2]+money[i],l2[i-1]) 
    answer = max(max(l),max(l2))
    return answer
    #초기화
    # total = 0
    # house = [(x[1],x[0]) for x in enumerate(money)]
    # visit = dict()
    # size = len(money)
    # house.sort(reverse=True)
    # for info in house:
    #     cash, no = info
    #     pre = size-1 if no-1<0 else no-1
    #     nxt = 0 if no + 1 >= size else no+1
    #     if visit.get(nxt,0) != 0 or visit.get(pre,0) != 0: continue
    #     total += cash
    #     visit[no] = 1
    # return total