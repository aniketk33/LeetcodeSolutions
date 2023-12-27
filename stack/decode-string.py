def decode_str(s):
    stack = []

    for char in s:
        if char != ']':
            stack.append(char)
        else:
            sub_str = ''
            while stack[-1] != '[':
                # after popping from the stack, the last char popped should be the first in the substring
                sub_str = stack.pop() + sub_str

            # pop the '[' char
            stack.pop()

            # get the integer
            k = ''
            # iterate till the char is a digit
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * sub_str)

    return ''.join(stack)


res = decode_str('3[a]2[bc]')
print(res)
