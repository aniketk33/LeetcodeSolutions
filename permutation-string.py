def permutation_string(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_arr, s2_arr = [0] * 26, [0] * 26
    # for s1 array
    for i in range(len(s1)):
        s1_arr[ord(s1[i]) - ord('a')] += 1
        s2_arr[ord(s2[i]) - ord('a')] += 1

    # creating a variable to store the match count
    matches = 0
    # looping through the alphabets
    for i in range(26):
        matches += 1 if s1_arr[i] == s2_arr[i] else 0

    left_ptr = 0
    for right_ptr in range(len(s1), len(s2)):
        if matches == 26:
            return True
        # adding characters to the window
        index = ord(s2[right_ptr]) - ord('a')
        s2_arr[index] += 1
        if s1_arr[index] == s2_arr[index]:
            matches += 1
        elif s1_arr[index] + 1 == s2_arr[index]:
            matches -= 1

        # removing characters from the window
        index = ord(s2[left_ptr]) - ord('a')
        s2_arr[index] -= 1
        if s1_arr[index] == s2_arr[index]:
            matches += 1
        elif s1_arr[index] - 1 == s2_arr[index]:
            matches -= 1
        left_ptr += 1
    return matches == 26


s1 = "ab"
s2 = "eidboaooo"
res = permutation_string(s1, s2)
print(res)
