from collections import defaultdict


# extra space solution
def lemonade_change(bills):
    change = defaultdict(int)

    for bill in bills:
        if bill == 5:
            change[bill] += 1
            continue
        if bill == 10:
            if change[5] <= 0:
                return False
            change[5] -= 1
            change[bill] += 1
        elif bill == 20:
            # if there are no 10$ bills then check for three 5$ bills
            if change[10] <= 0:
                if change[5] < 3:
                    return False
                change[5] -= 3
                change[bill] += 1
            elif change[5] <= 0:
                return False
            else:
                change[5] -= 1
                change[10] -= 1
                change[bill] += 1

    return True


# constant space solution
def lemonade_change_2(bills):
    five_dollars = 0
    ten_dollars = 0

    for bill in bills:
        # keep storing 5$
        if bill == 5:
            five_dollars += 1
        elif bill == 10:
            # check if there is a 5$ bill
            if five_dollars > 0:
                five_dollars -= 1
                # store the 10$ bill
                ten_dollars += 1
            else:
                return False
        elif bill == 20:
            # check if 10$ and 5$ bills are present
            if ten_dollars > 0 and five_dollars > 0:
                ten_dollars -= 1
                five_dollars -= 1
            # also, three or more 5$ bills work
            elif five_dollars >= 3:
                five_dollars -= 3
            else:
                return False

    return True


b = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
# bills = [5,5,10, 20, 20]
# res = lemonade_change(b)
res = lemonade_change_2(b)
print(res)
