from collections import defaultdict, deque


def word_ladder(begin_word, end_word, word_list):
    # base case
    if end_word not in word_list:
        return 0

    result = 1
    # to create hashmap of all the possible patterns of the given word
    neighbor_dict = defaultdict(list)

    for word in word_list:
        for index in range(len(word)):
            pattern = word[:index] + '*' + word[index + 1:]
            # for the given pattern add the particular word
            neighbor_dict[pattern].append(word)

    bfs_queue = deque([begin_word])
    visited_word = {begin_word}

    while bfs_queue:
        # loop for every level
        for i in range(len(bfs_queue)):
            word = bfs_queue.popleft()
            if word == end_word:
                return result
            # if not then add its neighbor to the queue
            for index in range(len(word)):
                pattern = word[:index] + '*' + word[index + 1:]
                # loop through its neighbor and if not visited then add to the queue
                for neighbor in neighbor_dict[pattern]:
                    if neighbor not in visited_word:
                        bfs_queue.append(neighbor)
                        visited_word.add(neighbor)

        result += 1

    # because if the path is found then it will be returned from the loop
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
res = word_ladder(beginWord, endWord, wordList)
print(res)
