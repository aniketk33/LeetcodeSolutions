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


flowerbed = [1, 0, 0, 0, 0, 0, 1]
res = place_flowers(flowerbed, 2)
print(res)
