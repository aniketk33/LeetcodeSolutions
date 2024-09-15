# brute force approach O(n^2)
def largest_substring(s):
    count = -1

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j - i - 1 > count:
                    count = j - i - 1

    return count


def largest_substring_2(s):
    char_location = {}
    dist = -1

    for i in range(len(s)):
        c = s[i]
        if c in char_location:
            if i - char_location[c] - 1 > dist:
                dist = i - char_location[c] - 1
        else:
            char_location[c] = i

    return dist


# res = largest_substring('ygtqdztaduxlsaacrwgtewywwchlnqzgjxhqgdhybncgaifonbe')
res = largest_substring_2('ygtqdztaduxlsaacrwgtewywwchlnqzgjxhqgdhybncgaifonbe')
print(res)
