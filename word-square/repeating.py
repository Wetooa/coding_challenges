from multiprocessing import Process
from string import ascii_lowercase

from generate import generate_words_by_length

FILE_NAME = "./english-words/words_alpha.txt"

W = generate_words_by_length(FILE_NAME)


def display_word_square(word_square):
    print("-" * (len(word_square[0]) + 2))
    for row in word_square:
        print(f"|{"".join(row)}|")
    print("-" * (len(word_square[0]) + 2))


def generate_word_square(N, M):

    wt = W.get_trie(M)

    tr = [wt.root for _ in range(N)]
    tc = [wt.root for _ in range(M)]
    ws = [[" "] * M for _ in range(N)]

    def brute_force(i, j):

        if i == N:
            print(f"Found a/n {N}x{M} word square:")
            display_word_square(ws)
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


# N = int(input("Enter N: "))
# M = int(input("Enter M: "))
# generate_word_square(N, M)


def brute_force_square_with_tl(N, M):
    print(f"Generating word square of size {N}x{M}")
    process = Process(target=generate_word_square, args=(N, M))
    process.start()
    process.join(timeout=20)

    if process.is_alive():
        print(f"Process for {N}x{M} is still running, terminating it.")
        process.terminate()
        process.join()
    else:
        print("Finished within time.")
    print()


def compute_for_all():
    from time import sleep

    jobs = []
    R, C = 3, 10

    for i in range(R, C):
        for j in range(R, C):
            p = Process(target=brute_force_square_with_tl, args=(i, j))
            p.start()
            jobs.append(p)
            sleep(0.05)  # slight delay to avoid spawn congestion

    """
    Slight learning, python Process is already gonna run in parallel, so no need to use Pool
    """
    for job in jobs:
        job.join()


compute_for_all()
