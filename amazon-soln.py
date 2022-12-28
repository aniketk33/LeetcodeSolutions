class TestClass:

    def getpMatchingScore(self, username1, username2, p):
        # Write your code here
        valid_indices = 0
        username_pattern = ''
        for i in range(len(username2)):
            for j in range(i, len(username1), p):
                username_pattern += username1[j]

            # sorted_pattern = ''.join(sorted(username_pattern))
            # sorted_username2 = ''.join(sorted(username2))

            pattern_matched = ''
            for pattern in username_pattern:
                if pattern in username2:
                    pattern_matched += pattern

            if pattern_matched == username2:
                valid_indices += 1 
                username_pattern = ''

        return valid_indices

user1 = 'zxyzxxyz'
user2 = 'xxzy'
p = 1
sol = TestClass().getpMatchingScore(user1, user2, p)
print(sol)
    # while not username_matched:        
    #     username_pattern += username1[i]
    #     i = i + p
    #     if i > len(username1) - 1:
    #         i = i - p
    #     if list(username_pattern).sort() == list(username2).sort():
    #         # username_matched = True
    #         valid_indices += 1