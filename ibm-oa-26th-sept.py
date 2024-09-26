"""
I had to check in a string where no two adjacent characters are either the same or adjacent to the alphabet.
For example, 'aa' or 'ab'. I had to perform operations to match the required conditions and
return the min operations required
"""


def min_operations(s):
    def is_beautiful(a, b):
        return a == b or abs(ord(a) - ord(b)) == 1

    operations = 0
    curr_idx = 0

    while curr_idx < len(s):
        if curr_idx > 0 and is_beautiful(s[curr_idx], s[curr_idx - 1]):
            operations += 1
            curr_idx += 2
        else:
            curr_idx += 1

    return operations


res1 = min_operations("abba")
print(res1)

"""2. It was SQL query where I had to join two tables and get data according to the condition. Below is the SQL Query:
"""
# SELECT email, COUNT(interest_flow) as bonds, ROUND(MIN(interest_flow),2) as min_interest_flow,
# ROUND(MAX(interest_flow), 2) as max_interest_flow, ROUND(AVG(interest_flow), 2) as avg_interest_flow
# FROM investors AS i
# JOIN portfolios AS p
# ON i.id = p. investor_id
# GROUP BY p. investor_id HAVING SUM(interest_flow) › 500000 ORDER BY email;
