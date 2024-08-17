from collections import Counter


def min_substring(original, check):
    check_counter = Counter(check)
    left, right = 0, 0
    curr_valid_window = {}
    result = (0, -(len(original) + 1))

    # required to check the valid character count in the current window
    required = len(check_counter.keys())
    satisfied = 0

    def get_min_result(left_idx, right_idx):
        prev_left_idx, prev_right_idx = result
        # base case
        if prev_right_idx < 0:
            return left_idx, right_idx

        # return if the previous length is shorter than the current length
        if prev_right_idx - prev_left_idx < right_idx - left_idx:
            return prev_left_idx, prev_right_idx
        # if both are same, then check lexicographically and return the smallest
        elif prev_right_idx - prev_left_idx == right_idx - left_idx:
            if original[prev_left_idx:prev_right_idx] > original[left_idx:right_idx]:
                return left_idx, right_idx
            else:
                return prev_left_idx, prev_right_idx
        else:
            return left_idx, right_idx

    while right < len(original):
        # only add valid characters to the current window
        if original[right] in check_counter:
            curr_valid_window[original[right]] = 1 + curr_valid_window.get(original[right], 0)
            if curr_valid_window[original[right]] == check_counter[original[right]]:
                satisfied += 1

            # remove valid characters until they are removed from the current window
            while satisfied == required:
                result = get_min_result(left, right + 1)
                # only decrease the count if present
                if original[left] in check_counter:
                    curr_valid_window[original[left]] -= 1
                    if curr_valid_window[original[left]] < check_counter[original[left]]:
                        satisfied -= 1

                left += 1

        right += 1

    return original[result[0]:result[1]]


res = min_substring('aa', 'aa')
print(res)
