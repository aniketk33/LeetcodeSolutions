# brute force approach
def relative_ranks(score: list):
    score_sorted = sorted(score, reverse=True)
    medal = {
        0: 'Gold Medal',
        1: 'Silver Medal',
        2: 'Bronze Medal'
    }

    for i in range(len(score_sorted)):
        idx = score.index(score_sorted[i])
        score[idx] = medal[i] if i <= 2 else str(i + 1)

    return score


def relative_ranks_2(score):
    score_sorted = sorted(score, reverse=True)
    medal = {
        0: 'Gold Medal',
        1: 'Silver Medal',
        2: 'Bronze Medal'
    }
    score_map = {}

    for i in range(len(score_sorted)):
        # store the value as index to map them later from the actual input
        score_map[score_sorted[i]] = medal[i] if i <= 2 else str(i + 1)

    return [score_map[s] for s in score]


res = relative_ranks([10, 3, 8, 9, 4])
print(res)
