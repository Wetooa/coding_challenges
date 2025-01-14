def kmp(text: str, pattern: str):

    lps = [0]
    i = 1
    j = 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            i += 1
            lps.append(j)
        elif j == 0:
            i += 1
            lps.append(0)
        else:
            j = lps[j - 1]

    res = []
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]

        if j == len(pattern):
            res.append(i - j)
            j = lps[j - 1]

    return res


def test_kmp():
    text = "abxabcabcaby"
    pattern = "abcaby"
    result = kmp(text, pattern)
    expected = [6]
    assert result == expected, f"Expected {expected}, but got {result}"

    text = "abcabcabcabc"
    pattern = "abc"
    result = kmp(text, pattern)
    expected = [0, 3, 6, 9]
    assert result == expected, f"Expected {expected}, but got {result}"

    text = "aabaaabaaac"
    pattern = "aabaaac"
    result = kmp(text, pattern)
    expected = [4]
    assert result == expected, f"Expected {expected}, but got {result}"

    print("All tests passed.")


if __name__ == "__main__":
    test_kmp()
