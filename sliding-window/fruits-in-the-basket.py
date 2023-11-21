from collections import defaultdict


def total_fruits(fruits):
    fruit_count = defaultdict(int)
    left_ptr, right_ptr = 0, 0
    result = 0
    curr_window_length = 0

    while right_ptr < len(fruits):
        # increment the current fruit count
        fruit_count[fruits[right_ptr]] += 1
        # increment the window size
        curr_window_length += 1

        # check if the hashmap is greater than 2 unique fruits
        while len(fruit_count) > 2:
            left_most_fruit = fruits[left_ptr]
            # decrement its count
            fruit_count[left_most_fruit] -= 1
            # decrement the window size
            curr_window_length -= 1
            # if its value equals zero then remove it
            if not fruit_count[left_most_fruit]:
                fruit_count.pop(left_most_fruit)
            left_ptr += 1

        result = max(result, curr_window_length)
        right_ptr += 1

    return result


res = total_fruits([0, 1, 2, 2])
print(res)
