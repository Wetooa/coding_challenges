for x in range(100, 0, -1):
    if x < ((100 - x) * 0.35):
        print(x)
        print(100 - x)
        break