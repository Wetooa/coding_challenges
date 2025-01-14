# An algorithm mainly used for finding the longest prefix starting at index i that is also a prefix of the entire string
# Can also be used for pattern matching


def pattern_matching(text, pattern):
    text = pattern + "$" + text

    return z_fn(text)[len(pattern) + 1 :]


def z_fn(text):
    N = len(text)
    z_box = [0]
    l = r = 0

    for i in range(1, N):
        # CASE 1: Outside of z-box
        if r < i:
            l = r = i
            while r < N and text[r] == text[r - l]:
                r += 1
            z_box.append(r - l)
            r -= 1
        # CASE 2: Inside of z-box
        else:
            offset = i - l

            # CASE 2.1: z-box item + current_index is less than or equal to r
            # we just copy
            if z_box[offset] + i <= r:
                z_box.append(z_box[offset])

            # CASE 2.2: z-box item + current_index is greater than r
            # we check for more
            else:
                l = i
                while r < N and text[r] == text[r - l]:
                    r += 1
                z_box.append(r - l)
                r -= 1

    return z_box


"abc$xbcabzabc"

pattern = "abc"
text = "xabcabzabc"

text = "aabxaabxcaabxaabxay"
print(z_fn(text))

# print(pattern_matching(text, pattern))
