DIGITS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def letter_combo(digits):
    result = []

    def backtrack(curr_idx, curr_str):
        if len(curr_str) == len(digits):
            result.append(curr_str)
            return

        letters = DIGITS[digits[curr_idx]]
        for letter in letters:
            backtrack(curr_idx + 1, curr_str + letter)

    if digits:
        backtrack(0, '')

    return result


d = '23'
res = letter_combo(d)
print(res)
