import random


def pick(switchs):
    num_doors = 1000

    val: list[int] = [0] * (num_doors - 1) + [1]
    random.shuffle(val)

    first_choice = random.randint(0, num_doors - 1)

    return val[first_choice] if not switch else not val[first_choice]


n = 1000

switch = sum([pick(1) for _ in range(n)])
keep = sum([pick(0) for _ in range(n)])

print("Percentage when switching:", switch / n)
print("Percentage when keeping:", keep / n)
