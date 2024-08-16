from collections import defaultdict


def least_consecutive(cards):
    card_dict = defaultdict(int)
    left, right = 0, 0
    smallest = float('inf')

    while right < len(cards):
        card_dict[cards[right]] = 1 + card_dict.get(cards[right], 0)
        while card_dict[cards[right]] >= 2:
            smallest = min(smallest, right - left + 1)
            card_dict[cards[left]] -= 1
            left += 1
        right += 1

    return -1 if smallest == float('inf') else smallest


res = least_consecutive([3, 4, 2, 3, 4, 7])
# res = least_consecutive([1, 2, 3, 1, 3, 2])
print(res)
