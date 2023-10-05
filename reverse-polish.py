def operand_result(val1, val2, operand):
    if operand == '+':
        return val1 + val2
    elif operand == '-':
        return val1 - val2
    elif operand == '/':
        return int(val1 / val2)
    else:
        return val1 * val2


def reverse_polish_notation(tokens_arr):
    result_stack = []
    operands = ['+', '-', '/', '*']
    for token in tokens_arr:
        if token in operands:
            # first pop is second value
            val_2 = int(result_stack.pop())
            # second pop is first value
            val_1 = int(result_stack.pop())
            result = operand_result(val_1, val_2, token)
            result_stack.append(result)
        else:
            result_stack.append(token)

    return int(result_stack.pop())


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = reverse_polish_notation(tokens)
print(res)
