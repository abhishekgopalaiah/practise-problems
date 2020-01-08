def isBalanced(s):
    if len(s) <= 0:
        return 'NO'
    d = {')': '(', '}': '{', ']': '['}
    opening = ['(', '{', '[']
    stack = []
    for i in s:
        if len(stack) <= 0:
            stack.append(i)
        elif i in opening:
            stack.append(i)

        elif stack[-1] == d[i]:
            stack.pop(-1)
        else:
            stack.append(i)
    if len(stack) > 0:
        return 'NO'
    else:
        return 'YES'
