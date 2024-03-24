import random

repeater = 0
same_bday_counter = 0
while repeater != 100000:
    babies = []
    babies_count = 23
    checker = False
    for x in range(babies_count):
        babies.append(random.randint(1,365))
    for x in range(len(babies)):
        for y in range(len(babies)):
            if y == x:
                break
            else:
                if babies[x] == babies[y]:
                    checker = True
    if checker:
        same_bday_counter += 1
    repeater += 1


print(f'Birthday Paradox - Babies Count = {babies_count}')
print(f'{same_bday_counter/repeater*100}%')