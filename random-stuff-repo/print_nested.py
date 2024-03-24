def printList(l):
    if type(l) != list:
        print(l, end = " ")
    else:
        for x in range(len(l)):
            printList(l[x])

l = [[[1, 2, [3, 1, 2], 2, [1, 2, 3, 4, [1, [2, 3, 1], 1, 5], 2, 3, [4, 2, 3], 1, 3], 3, 4], 1, 1], [1, 2, [3, 1, 2], 2, [1, 2, 3, 4, [1, [2, 3, 1], 1, 5], 2, 3, [4, 2, 3], 1, 3], 3, 4]]

print(l)
printList(l)