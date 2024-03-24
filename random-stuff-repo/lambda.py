# learn this cool shit

from tkinter import X


l = list(map(lambda x:x*x, list(range(10))))
l = list(filter(lambda x: x > 10 and x < 80, l))

# cool shorter ver
print(list(filter(lambda x: x > 10 and x < 80, list(map(lambda x:x*x, list(range(10)))))))


print(list(map(lambda x:x**2, [x for x in range(30)])))
print(list(filter(lambda x:x % 2 == 0, [x**2 for x in range(30)])))
print(len(list(filter(lambda x:x + 450 == int(''.join([str(x)[y-1] for y in range(len(str(x)), 0, -1)])), [x for x in range(0, 100000)]))))
