_end = '_end_'


class Trie:

    def __init__(self, *words):
        self.root = {}
        self.words = words
        for word in words:
            curr = self.root
            for letter in word:
                curr = curr.setdefault(letter, {})
            curr[_end] = _end

    def in_trie(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        print('final check for leaf')
        return _end in curr

    def suggestion(self, prefix):
        print(f"Search {self.words} for prefix '{prefix}'")
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return ''
            curr = curr[letter]
        if _end in curr and len(curr) == 1:
            return ''
        sug = []
        self.dfs(curr, prefix, sug)
        sug.remove(prefix)
        print(sug)

    def dfs(self, start, prefix, sug):
        for key in start:
            next = start[key]
            if next == _end:
                sug.append(prefix)
            else:
                word = prefix + key
                self.dfs(next, word, sug)

    def _dfs(self, start, prefix):
        for key in start:
            next = start[key]
            if next == _end:
                print(prefix)
            else:
                word = prefix + key
                self._dfs(next, word)

    def __repr__(self):
        return str(self.root)
