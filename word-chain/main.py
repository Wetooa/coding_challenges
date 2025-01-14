import collections
import string

FILE_NAME = "./english-words/words_alpha.txt"

alphabet = string.ascii_lowercase
file_content = open(FILE_NAME).read().strip()
file_words = file_content.split("\n")
all_words = collections.defaultdict(list)

for word in file_words:
    all_words[len(word)].append(word)

print("Total words in the dictionary:", len(file_words))

for word_length, words in sorted(all_words.items()):
    print(f"Length {word_length}: {len(words)} words")


print(
    """
===================================================================
 _    _               _   _____ _           _       
| |  | |             | | /  __ \\ |         (_)      
| |  | | ___  _ __ __| | | /  \\/ |__   __ _ _ _ __  
| |/\\| |/ _ \\| '__/ _` | | |   | '_ \\ / _` | | '_ \\ 
\\  /\\  / (_) | | | (_| | | \\__/\\ | | | (_| | | | | |
 \\/  \\/ \\___/|_|  \\__,_|  \\____/_| |_|\\__,_|_|_| |_|
===================================================================
"""
)

start_word = input("Input start word: ")
end_word = input("Input end word: ")

if len(start_word) != len(end_word):
    print("Words must have the same length")
    exit()

N = len(start_word)

if start_word not in all_words[N] or end_word not in all_words[N]:
    print("Words not in the dictionary")
    exit()


q = collections.deque([start_word])
v = {start_word: ""}


while q:
    word = q.popleft()

    if word == end_word:
        break

    for i in range(N):
        for char in alphabet:
            if char == word[i]:
                continue

            new_word = word[:i] + char + word[i + 1 :]

            if new_word not in v and new_word in all_words[N]:
                v[new_word] = word
                q.append(new_word)

if end_word not in v:
    print("No solution found")
    exit()

sol = []
curr_word = end_word

while curr_word != start_word:
    sol.append(curr_word)
    curr_word = v[curr_word]

sol.append(curr_word)

print(" -> ".join(sol[::-1]))
