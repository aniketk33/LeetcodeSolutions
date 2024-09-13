def path_crossing(path):
    visited = set()
    x = y = 0

    # you always start from the origin
    visited.add((x, y))

    for p in path:
        if p == 'N':
            y += 1
        elif p == 'S':
            y -= 1
        elif p == 'E':
            x += 1
        else:
            x -= 1
        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False


res = path_crossing('NES')
print(res)
