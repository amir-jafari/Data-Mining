class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def autocomplete(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        suggestions = []

        def dfs(node, path):
            if node.is_end_of_word:
                suggestions.append(''.join(path))
            for char, child_node in node.children.items():
                dfs(child_node, path + [char])

        dfs(current, list(prefix))
        return suggestions


# Example Usage
trie = Trie()
words = ["cat", "car", "cart", "carbon", "dog", "dove", "door"]
for word in words:
    trie.insert(word)

prefix = "car"
print(f"Words starting with '{prefix}': {trie.autocomplete(prefix)}")