# LeetCode #20 - Valid Parentheses
def is_valid(s):
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in pairs:
            stack.append(pairs[c])  # push the closer we expect
        elif not stack or stack.pop() != c:
            return False
    return not stack  # leftover openers mean invalid


if __name__ == '__main__':
    print(is_valid('()[]{}'))  # True
    print(is_valid('(()){}'))  # True
    print(is_valid('(]'))      # False
    print(is_valid('([)]'))    # False
    print(is_valid('(('))      # False
    print(is_valid(''))        # True
