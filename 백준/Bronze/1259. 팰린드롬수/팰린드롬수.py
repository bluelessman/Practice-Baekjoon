while True:
    N = input()
    isTrue = True
    if N == '0':
        break
    else:
        for i in range(len(N)//2):
            if N[i] != N[-(i+1)]:
                isTrue = False
                continue
        if isTrue:
            print("yes")
        else:
            print("no")
        
        