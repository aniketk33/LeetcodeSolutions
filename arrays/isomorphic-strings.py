def is_isomorphic(s: str, t: str):
    map_ST, map_TS = {}, {}

    for char1, char2 in zip(s, t):
        # check if any of the hashmap keys map to different char besides the old one
        if ((char1 in map_ST and map_ST[char1] != char2) or
                char2 in map_TS and map_TS[char2] != char1):
            return False

        # map each other in both the ways
        map_ST[char1] = char2
        map_TS[char2] = char1

    return True


res = is_isomorphic('egg', 'add')
print(res)
