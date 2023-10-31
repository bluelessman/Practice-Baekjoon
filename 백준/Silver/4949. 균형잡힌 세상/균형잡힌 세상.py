import sys
while True:
    s = sys.stdin.readline().rstrip()
    stack = []
    if s =='.':
        break
    else:
        isTrue = True
        for i in s:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')' or i == ']':
                if not stack:
                    print('no')
                    isTrue = False
                    break
                elif i == ')':
                    if stack.pop()!='(':
                        print('no')
                        isTrue = False
                        break
                elif i == ']':
                    if stack.pop()!='[':
                        print('no')
                        isTrue = False
                        break
        if isTrue:
          if stack:
            print('no')
          else:
            print('yes')