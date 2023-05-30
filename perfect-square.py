def perfect_square(num):
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        estimated_square = mid * mid
        if estimated_square == num:
            return True
        if estimated_square > num:
            right = mid - 1
        else:
            left = mid + 1

    return False


number = 9
if perfect_square(number):
    print(f'{number} is a perfect square')
else:
    print(f'{number} is not a perfect square')
