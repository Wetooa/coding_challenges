import functools
import random
import numpy as np

# pang fix


def hamming(bits):
    return functools.reduce(lambda x, y: x ^ y, [
        i for i, bit in enumerate(bits) if bit])


# made random bits
bits = np.random.randint(0, 2, 256)
print(bits)
print(np.matrix([bits[i:i+4] for i in range(0, len(bits), 4)]))
print([i for i, bit in enumerate(bits) if bit])

# searched for the err
err = hamming(bits)
print(err)

# reversed the err bit
bits[err] = not bits[err]
err = hamming(bits)
print(bits)
print(err)

# reverse random bit for fun
bits[2] = not bits[2]
err = hamming(bits)
print(bits)
print(err)
