from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def insert_word(self, word):
        curr = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end_of_word = True


def word_search_2(board: List[List[str]], words: List[str]):
    # create tree
    root = TrieNode()
    for word in words:
        root.insert_word(word)

    # get the total rows and columns of the board
    ROWS, COLUMNS = len(board), len(board[0])
    visited_path = result = set()

    def dfs(curr_row, curr_column, curr_node: TrieNode, curr_word: str):
        # boundary cases
        if (curr_row < 0 or curr_column < 0 or
                curr_row == ROWS or curr_column == COLUMNS or
                board[curr_row][curr_column] not in curr_node.children or
                (curr_row, curr_column) in visited_path):
            return

        curr_board_word = board[curr_row][curr_column]

        # add the visited board location
        visited_path.add((curr_row, curr_column))

        # update the curr node to its child
        curr_node = curr_node.children[curr_board_word]

        # add the visited board word to the current word
        curr_word += curr_board_word

        # check if the curr_node is the last char of the word and if so, add to the result
        if curr_node.end_of_word:
            result.add(curr_word)

        # apply dfs to all the adjacent location
        dfs(curr_row + 1, curr_column, curr_node, curr_word)
        dfs(curr_row - 1, curr_column, curr_node, curr_word)
        dfs(curr_row, curr_column + 1, curr_node, curr_word)
        dfs(curr_row, curr_column - 1, curr_node, curr_word)

        # remove the visited board location
        visited_path.remove((curr_row, curr_column))

    for row in range(ROWS):
        for column in range(COLUMNS):
            dfs(row, column, root, "")

    return list(result)


input_board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
input_words = ["oath", "pea", "eat", "rain"]
res = word_search_2(input_board, input_words)
print(res)
