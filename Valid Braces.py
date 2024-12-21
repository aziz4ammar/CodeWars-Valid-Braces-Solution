def valid_braces(string):
    stack = []
    brace_map = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in brace_map.values():
            stack.append(char)
        elif char in brace_map.keys():
            if not stack or stack.pop() != brace_map[char]:
                return False
    return not stack