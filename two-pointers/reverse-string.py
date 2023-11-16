def reverse(s: list):
    left_ptr, right_ptr = 0, len(s) - 1
    while left_ptr <= right_ptr:
        s[left_ptr], s[right_ptr] = s[right_ptr], s[left_ptr]
        left_ptr += 1
        right_ptr -= 1


input_s = ["h", "e", "l", "l", "o"]
print(f'Before reversing: {input_s}')
reverse(input_s)
print(f'After reversing: {input_s}')
