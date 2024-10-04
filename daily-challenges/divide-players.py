from collections import Counter


def divide_players(skill):
    total = sum(skill)
    players = len(skill)
    teams = players // 2
    team_sum = total / teams
    if total % teams != 0:
        return -1

    chemistry = 0
    team_sum = int(team_sum)
    skill_count = Counter(skill)
    for val in skill:
        compliment = team_sum - val
        # both the values should be same to make the pairs
        if skill_count[compliment] != skill_count[val]:
            return -1
        if skill_count[val] > 0 and skill_count[compliment] > 0:
            chemistry += val * compliment
            skill_count[val] -= 1
            skill_count[compliment] -= 1

    return chemistry


# using two pointer approach
def divide_players_2(skill):
    # after sorting, it is easy to form pairs
    skill.sort()
    left, right = 0, len(skill) - 1
    team_sum = skill[left] + skill[right]
    chemistry = 0

    while left < right:
        if skill[left] + skill[right] != team_sum:
            return -1
        chemistry += skill[left] * skill[right]
        left += 1
        right -= 1

    return chemistry


# res = divide_players([3, 2, 5, 1, 3, 4])
res = divide_players_2([3, 2, 5, 1, 3, 4])
# res = divide_players([1, 1, 1, 2, 3, 3, 3, 7, 7, 8, 8, 8, 9, 9])
print(res)
