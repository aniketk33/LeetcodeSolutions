"""Amazon's AWS provides fast and efficient server solutions. The developers want to stress-test the quality of the
servers' channels. They must ensure the following:
• Each of the packets must be sent via a single channel.
• Each of the channels must transfer at least one packet.
The quality of the transfer for a channel is defined by the median
of the sizes of all the data packets sent through that channel.
Note: The median of an array is the middle element if the array is sorted in non-decreasing order.
If the number of elements in the array is even, the median is the
average of the two middle elements. Find the maximum possible sum of the quality of all channels, If the answer is a
floating-point value, round it to the next higher integer.
Example packets = [1, 2, 3, 4, 5] channels = 2
At least one packet has to go through each of the 2 channels.
One maximal solution is to transfer packets {1, 2, 3, 4} through channel 1 and packet {5} through channel 2."""
from collections import deque

import math


# problem 1.
def max_quality(packets, channels):
    packets.sort()
    max_sum = 0

    # start from the right end of the sorted list and keep adding
    start_idx = len(packets) - channels + 1
    for i in range(start_idx, len(packets)):
        max_sum += packets[i]

    # get the median from the remaining items in the list
    remaining_packets = packets[:start_idx]
    mid_idx = len(remaining_packets) // 2
    if mid_idx % 2 == 0:
        median = remaining_packets[mid_idx]
    else:
        median = (remaining_packets[mid_idx] + remaining_packets[mid_idx - 1]) // 2
        median = math.ceil(median)

    max_sum += median

    return max_sum


res = max_quality([1, 2, 3, 4, 5], 2)
print(res)

"""To promote physical fitness, on the portal they launched a "GetFit" tournament consisting of n sprints. Each 
sprint lasts for a given number of days and includes several tasks such as push-ups, running, etc. Some tasks are 
scheduled for each day of the sprint. The ith sprint lasts for days[i] days, and each sprint starts just after the 
other. That is, if the ith sprint ends on day d, the (i + 1)th sprint starts on day (d + 1). During each sprint, 
completing the required tasks scheduled on the jth day of the sprint earns the participant / points.
The tournaments are periodic, i.e, as soon as the last sprint of a tournament ends, 
the first sprint of the next tournament begins. Each tournament, however, has the same schedule of sprints.
More formally, the tournament schedule can be considered cyclic in nature and after the last sprint, 
the first sprint starts again.
An employee decides to participate. However, due to a tight schedule, the employee cannot complete all tasks every day. 
Instead, the employee will complete the tasks of exactly k consecutive days, 
hoping to achieve the maximum number of points.
Given the sprint days of n sprints, and the number of days for which the employee competes for k, 
find the maximum points the employee can score. The training can start and end on any day of any sprint.
Note:
• k is guaranteed to be less than the total number of days for which the sprints last.
• Also, it is not necessary to start and end the training in the same tournament.
• A sprint here denotes a set of activities performed in a particular time period
Example
There are n = 3 sprints, the number of days of each sprint are days = [2,3,2], and k= 4.
The maximum number of points that can be attained = 2 + 1 + 2 + 3 = 8. One choice is to start on
the last day of the first sprint and end on the last day of the second sprint.

Constraints
• 1 ≤ n≤ 10^5
• 1 ≤ days,≤105, i= 1, 2, ., ท
• 1 <= days[1]+ days[2]+ .... + days[n]
 1 <= days[1]+ days[2]+ .... + days[n]
"""


# this solution throws a memory error when the days array is huge
def get_max_points(days, k):
    # create total days for given sprint
    total_days = [i for day in days for i in range(1, day + 1)]
    total_days.extend(total_days[:k])

    curr_points = sum(total_days[:k])
    max_points = curr_points
    i = 0

    while i + k < len(total_days):
        curr_points -= total_days[i]
        curr_points += total_days[i + k]
        i += 1
        max_points = max(max_points, curr_points)

    return max_points


# optimal solution
def get_max_points_2(days, k):
    if k == 0:
        return 0

    # to create a cyclic nature of the sprint, add the first value to the end
    days.append(days[0])

    curr_queue = deque()
    max_points = 0
    curr_points = 0

    for i in days:
        for j in range(1, i + 1):
            if len(curr_queue) < k:
                curr_points += j
                curr_queue.append(j)
            else:
                curr_points -= curr_queue.popleft()
                curr_points += j
                curr_queue.append(j)

            max_points = max(max_points, curr_points)

    return max_points


# result = get_max_points([7, 4, 6, 3, 5], 8)
result = get_max_points_2([7, 4, 6, 3, 5], 8)
print(result)
