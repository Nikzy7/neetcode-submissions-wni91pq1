class Trie:
    def __init__(self):
        self.children = dict()
        self.is_word = bool()

    def add_word(self, word):
        cur = self

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]

        cur.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.add_word(word)

        words_found = set()
        visited = set()

        def dfs(r, c, node, word):
            if r not in range(rows) or c not in range(cols):
                return

            if (r, c) in visited:
                return

            if board[r][c] not in node.children:
                return

            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word:
                words_found.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visited.remove((r, c))

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(words_found)
