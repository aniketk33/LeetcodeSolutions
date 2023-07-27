def longest_common_prefix(str_arr):
    if len(str_arr) == 1:
        return str_arr[0]
    result = ''
    for i in range(len(str_arr[0])):
        for s in str_arr:
            if len(s) == i or str_arr[0][i] != s[i]:
                return result

        result += str_arr[0][i]

    return result


strs = ["flower", "flow", "flight"]
res = longest_common_prefix(strs)
print(res)
