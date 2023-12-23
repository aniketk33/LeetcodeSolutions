from collections import deque


def push_dominoes(d):
    dominoes = list(d)
    q = deque()

    # add all the forces to the queue
    for i, val in enumerate(dominoes):
        if val != '.':
            q.append((i, val))

    while q:
        idx, force = q.popleft()
        # for left force
        if force == "L" and idx > 0 and dominoes[idx - 1] == ".":
            # change it to left and append the new force
            dominoes[idx - 1] = "L"
            q.append((idx - 1, "L"))
        elif force == "R":
            # check if the empty domino is in between left and right force
            if idx + 1 < len(dominoes) and dominoes[idx + 1] == ".":
                if idx + 2 < len(dominoes) and dominoes[idx + 2] == "L":
                    # remove the current right and do not change the next domino i.e the i+1
                    q.popleft()
                else:
                    q.append((idx + 1, "R"))
                    dominoes[idx + 1] = "R"

    return ''.join(dominoes)


res = push_dominoes('.......L.L')
print(res)
