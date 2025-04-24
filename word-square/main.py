from generate import generate_words_by_length

FILE_NAME = "./english-words/words_alpha.txt"

W = generate_words_by_length(FILE_NAME)


def display_word_square(word_square):
    for word in word_square:
        print(f"|{word}|")
    print()


def generate_word_square(rows, cols):

    wt = W.get_trie(cols)

    tries = [wt.root for _ in range(cols)]
    ws = ["" for _ in range(rows)]
    v = set()

    def brute_force(index):
        if index == rows:

            if not any("".join(w) in v for w in zip(*ws)):
                print("Found a word square:")
                display_word_square(ws)
                print()
                return True

            return False

        possible_words = []

        def inner_brute_force(node, index, prefix):
            if node.is_end_of_word:
                possible_words.append(prefix)
                return

            prev = tries[index]
            for c, child in node.letters.items():
                if c in tries[index].letters:
                    tries[index] = tries[index].letters[c]
                    inner_brute_force(child, index + 1, prefix + c)
                    tries[index] = prev

        inner_brute_force(wt.root, 0, "")

        copy = [a for a in tries]

        for word in possible_words:
            if word in v:
                continue

            for i, c in enumerate(word):
                tries[i] = tries[i].letters[c]
            v.add(word)
            ws[index] = word

            if brute_force(index + 1):
                return True

            for i, c in enumerate(copy):
                tries[i] = c
            v.remove(word)
            ws[index] = ""

    brute_force(0)


W.describe()


N = int(input("Enter N: "))
M = int(input("Enter M: "))
generate_word_square(N, M)
