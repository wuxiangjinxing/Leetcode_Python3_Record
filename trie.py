# trie(prefix tree) is an ordered tree that stores keys used in strings

class Trie:
    root = {}
    END = '/'
    def add(self, word):
        node = self.root
        for c in word:
            node=node.setdefault(c,{})
        node[self.END] = None
 
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.END in node
