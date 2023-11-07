def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == ")":
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True