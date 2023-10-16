"""A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
in a dataset of strings. There are various applications of this data structure, such as autocomplete and
spellchecker."""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        # initialize an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                # add the char in the current tree with empty node
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]

        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True


# Your Trie object will be instantiated and called as such:
input_word = 'apple'
input_prefix = 'app'
obj = Trie()
obj.insert(input_word)
param_2 = obj.search(input_word)
param_3 = obj.startsWith(input_prefix)
print(param_2, param_3)
