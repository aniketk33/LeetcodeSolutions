def string_great(s: str):
    result = []

    for c in s:
        # check for two conditions before adding to the stack
        if result and ((c.isupper() and result[-1].islower() and c.lower() == result[-1].lower())
                       or c.islower() and result[-1].isupper() and c.lower() == result[-1].lower()):
            result.pop()
        else:
            result.append(c)

    return ''.join(result)


res = string_great('abBA')
print(res)
