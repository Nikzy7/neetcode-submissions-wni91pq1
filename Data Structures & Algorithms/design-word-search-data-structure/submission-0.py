class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word_finished = bool()


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.is_word_finished = True

    def search(self, word: str) -> bool:
        cur = self.root

        queue = deque()
        queue.append(cur)

        ch_ptr = 0

        while queue and ch_ptr != len(word):
            total_to_pop = len(queue)

            atleast_one_found = False

            for _ in range(total_to_pop):
                cur = queue.popleft()

                if word[ch_ptr] == ".":
                    for child in cur.children:
                        queue.append(cur.children[child])
                        atleast_one_found = True
                elif word[ch_ptr] in cur.children:
                    queue.append(cur.children[word[ch_ptr]])
                    atleast_one_found = True

            if not atleast_one_found:
                return False
            ch_ptr += 1

        # finding atleast one end
        ends = False
        while queue:
            cur = queue.popleft()
            if cur.is_word_finished:
                ends = True

        return (True if ch_ptr == len(word) else False) if ends else False
