from typing import List


# modifying the given array
def min_cost(costs: List[int]):
    # e.g., [10,15,20] 0
    # append 0 (indicating the top of the floor)
    costs.append(0)

    # starting from the 3rd last element in the array and getting the cost of single and double jump
    for i in range(len(costs) - 3, -1, -1):
        # current + next
        single_jump_cost = costs[i] + costs[i + 1]
        # current + next to next
        double_jump_cost = costs[i] + costs[i + 2]
        # store the min of both the jumps at the current location
        costs[i] = min(single_jump_cost, double_jump_cost)

    # return the min cost starting from 1st or 2nd stair position
    return min(costs[0], costs[1])


# without modifying the given array
def min_cost_2(cost: List[int]):
    one = two = 0
    for i in range(2, len(cost) + 1):
        temp = one
        one = min(one + cost[i - 1], two + cost[i - 2])
        two = temp
    return one


res = min_cost_2([10, 15, 20])
print(res)
