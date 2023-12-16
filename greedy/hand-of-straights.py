import heapq


def hand_of_straights(cards, group_size):
    if len(cards) % group_size:
        return False

    cards_count = {}
    for card in cards:
        cards_count[card] = 1 + cards_count.get(card, 0)

    min_heap = list(cards_count.keys())
    heapq.heapify(min_heap)

    while min_heap:
        min_val = min_heap[0]

        for i in range(min_val, min_val + group_size):
            # the cards need to be consecutive, so this check is required as the above is a range function
            if i not in cards_count:
                return False
            cards_count[i] -= 1
            if cards_count[i] == 0:
                # before popping check if it is the min value of the heap or not
                if i != min_heap[0]:
                    return False
                heapq.heappop(min_heap)

    return True


res = hand_of_straights([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
print(res)
