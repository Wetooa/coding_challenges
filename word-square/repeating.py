from string import ascii_lowercase
from generate import generate_words_by_length

FILE_NAME = "./english-words/words_alpha.txt"

W = generate_words_by_length(FILE_NAME)


def display_word_square(word_square):
    for row in word_square:
        print(f"|{"".join(row)}|")
    print()


def generate_word_square(N, M):

    wt = W.get_trie(M)

    tr = [wt.root for _ in range(N)]
    tc = [wt.root for _ in range(M)]
    ws = [[" "] * M for _ in range(N)]

    def brute_force(i, j):
        display_word_square(ws)

        if i == N:
            print("Found a word square:")
            display_word_square(ws)
            print()
            return True

        a = tr[i]
        b = tc[j]
        for char in ascii_lowercase:
            if char in a.letters and char in b.letters:
                ws[i][j] = char
                tr[i] = a.letters[char]
                tc[j] = b.letters[char]

                if brute_force((i + (j + 1 == M)), (j + 1) % M):
                    return True

                ws[i][j] = " "
                tr[i] = a
                tc[j] = b

    brute_force(0, 0)


W.describe()


N = int(input("Enter N: "))
M = int(input("Enter M: "))
generate_word_square(N, M)
