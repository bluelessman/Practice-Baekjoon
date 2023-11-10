from itertools import combinations
def solution(distance, rocks, n):
    #초기화
    answer = 0
    start, end = 0, distance
    rocks.sort()
    rocks.append(distance)
    #알고리즘
    while start <= end:
        mid = (start+end)//2
        del_stones = 0
        pre_stone = 0
        for rock in rocks:
            if rock - pre_stone < mid:
                del_stones += 1
            else: 
                pre_stone = rock
            if del_stones > n:
                break
        
        if del_stones > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    #답안
    return answer