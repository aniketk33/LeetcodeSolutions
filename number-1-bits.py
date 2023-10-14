def hamming_weight(n):
    """using % operator"""
    result = 0
    while n:
        result += n % 2
        # shift bit by one to the right
        n = n >> 1

    return result


def hamming_weight_2(n):
    """using &(logical AND) operator"""
    result = 0
    while n:
        result += n & 1
        # shift bit by one to the right
        n = n >> 1

    return result
