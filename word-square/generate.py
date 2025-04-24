from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class TrieNode:
    letters: dict = field(default_factory=lambda: defaultdict(TrieNode))
    is_end_of_word: bool = False


@dataclass
class Trie:
    root: TrieNode = field(default_factory=TrieNode)
    size: int = 0
    words: list = field(default_factory=list)

    def add(self, word):
        current = self.root
        for c in word:
            current = current.letters[c]
        current.is_end_of_word = True

        self.size += 1
        self.words.append(word)

    def is_word(self, word):
        current = self.root
        for c in word:
            if c not in current.letters:
                return False
            current = current.letters[c]
        return current.is_end_of_word

    def get_all_words(self):
        return self.words

    def display_all_words(self):

        def _display_all_words(node, prefix):
            if node.is_end_of_word:
                print(prefix)
            for c, child in node.letters.items():
                _display_all_words(child, prefix + c)

        _display_all_words(self.root, "")


class WordDict:
    def __init__(self):
        self.__words_by_length = defaultdict(Trie)

    def add(self, word):
        self.__words_by_length[len(word)].add(word)

    def get_trie(self, length):
        return self.__words_by_length[length]

    def is_word(self, word):
        return self.get_trie(len(word)).is_word(word)

    def display_all_words(self):
        for length, trie in self.__words_by_length.items():
            print(f"Words of length {length}:")
            trie.display_all_words()
            print()

    def describe(self):
        for length, trie in sorted(self.__words_by_length.items(), key=lambda x: x[0]):
            print(f"Words of length {length}: {trie.size}")


def generate_words_by_length(file_name):
    W = WordDict()
    with open(file_name) as f:
        for line in f:
            word = line.strip()
            W.add(word)

    print("Finished generating words")

    return W
