def verify(words, order):
    # create hashmap with order of given chars
    order_dict = {val: idx for idx, val in enumerate(order)}

    i = 0
    while i < len(words) - 1:
        # loop until two different chars
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                return False
            # if they are different and order is right then continue with the next adjacent pair
            if words[i][j] != words[i + 1][j]:
                if order_dict[words[i][j]] > order_dict[words[i + 1][j]]:
                    return False
                else:
                    break
        i += 1

    return True


res = verify(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
print(res)
