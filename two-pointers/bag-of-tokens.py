def bag_tokens(tokens, power):
    tokens.sort()
    left, right = 0, len(tokens) - 1
    score = 0

    while left <= right:
        if power >= tokens[left]:
            score += 1
            power -= tokens[left]
            left += 1
        # to decrease the score, the left should always be smaller than the right pointer.
        # consider the below example for an edge case
        elif score > 0 and left < right:
            # add the largest value to current power and decrease the score
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return score


res = bag_tokens([100, 200], 150)
print(res)
