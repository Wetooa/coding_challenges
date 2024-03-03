d: dict[int, str] = {0: "a", 1: "b", 2: "c"}
i = 0

if letter := d.get(i):
    print(f"{letter} is the letter")
else:
    print(f"Letter with index {i} does not exist")


sum, a, b = 0, 1, 2
if sum := sum + a + b:
    print(sum)
