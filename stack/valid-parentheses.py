"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""


def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack


def is_valid_2(s):
    valid_pairs = {'()', '[]', "{}"}
    stack = []

    for c in s:
        # keep appending opening parentheses
        if c in '({[':
            stack.append(c)
        # if the stack is empty or the pair is not found, then return false
        elif not stack or stack.pop() + c not in valid_pairs:
            return False

    return not stack


input_str = "(){[[((((((()))))))]]}[]"
# result = is_valid(input_str)
result = is_valid_2(input_str)
print(result)
