def restore(s):
    result = []
    if len(s) > 12:
        return []

    def backtrack(curr_idx, dot_count, curr_ip):
        if dot_count == 4 and curr_idx == len(s):
            # exclude the last dot
            result.append(curr_ip[:-1])
            return
        if dot_count > 4:
            return

        # check for the next 3 chars and prevent the out-of-bounds case
        for i in range(curr_idx, min(curr_idx + 3, len(s))):
            # check if it is less than 256 and there are no leading zeroes
            if int(s[curr_idx:i + 1]) < 256 and (curr_idx == i or s[curr_idx] != '0'):
                backtrack(i + 1, dot_count + 1, curr_ip + s[curr_idx:i + 1] + '.')

    backtrack(0, 0, '')
    return result


res = restore('25525511135')
print(res)
