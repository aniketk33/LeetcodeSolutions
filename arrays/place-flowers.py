def place_flowers(flower_bed, n):
    # add zeros at the start and end of the list
    temp = [0] + flower_bed + [0]

    # skip iteration for first and last value
    for i in range(1, len(temp) - 1):
        # if you find three consecutive zeros, then decrease n
        if temp[i - 1] == 0 and temp[i] == 0 and temp[i + 1] == 0:
            temp[i] = 1
            n -= 1

    return n <= 0


def place_flowers_2(flower_bed, n):
    idx = 0

    while idx < len(flower_bed):
        # check for three things
        # 1. if it is a 0
        # 2. if the prev value is 0
        # 3. the next value should be 0 too
        if (flower_bed[idx] == 0 and (idx == 0 or flower_bed[idx - 1] == 0) and
                (idx == len(flower_bed) - 1 or flower_bed[idx + 1] == 0)):
            flower_bed[idx] = 1
            n -= 1
        idx += 1

    return n <= 0


flowerbed = [1,0,0,0,0,1]
# res = place_flowers(flowerbed, 2)
res = place_flowers_2(flowerbed, 2)
print(res)
