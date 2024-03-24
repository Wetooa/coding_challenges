import random
from re import X
from tabnanny import check

counter = 0
win_counter = 0
while counter != 100000:
    prisoners = [x for x in range(100)]
    boxes = [x for x in range(100)]
    random.shuffle(boxes)
    
    # print(list(map(lambda x:[x, boxes.index(x)], boxes)))

    for x in prisoners:
        count = 50
        check_index = x
        while count != 0 and x != boxes[check_index]:
            # print(boxes[check_index])
            check_index = boxes[check_index]
            count -= 1
        if x != boxes[check_index]:
            break
    else:
        win_counter += 1
    counter += 1
print(win_counter, counter)