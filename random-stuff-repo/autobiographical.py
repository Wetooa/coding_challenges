def autobiographical_checker(splitted, num):
    checker = 0
    for x in range(len(splitted)):
        counter = 0
        for y in range(len(splitted)):
            if splitted[y] == x:
                counter += 1
        if splitted[x] == counter:checker += 1
    if checker == len(splitted):
        return True
    else:
        return False

num = 0
while len(str(num)) < 11:
    splitted = list(map(int, str(num)))
    result = autobiographical_checker(splitted, num)
    if result:print(num)
    num += 1
    