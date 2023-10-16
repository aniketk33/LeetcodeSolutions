class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                # add the char in the current tree with empty node
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]

        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(start_idx, curr_child_node):
            curr_node = curr_child_node

            for i in range(start_idx, len(word)):
                if word[i] == '.':
                    for child in curr_node.children.values():
                        # call recursively
                        if dfs(i+1, child):
                            return True
                        return False
                # a normal character
                else:
                    if word[i] not in curr_node.children:
                        return False
                    curr_node = curr_node.children[word[i]]

            return curr_node.end_of_word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
