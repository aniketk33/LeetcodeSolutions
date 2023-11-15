def num_pairs(rectangles):
    ratio_count = {}

    for width, height in rectangles:
        ratio = width / height
        ratio_count[ratio] = 1 + ratio_count.get(ratio, 0)

    result = 0
    for val in ratio_count.values():
        if val > 0:
            # formula to find the combination
            result += (val * (val - 1)) // 2

    return result


res = num_pairs([[4, 8], [3, 6], [10, 20], [15, 30]])
print(res)
