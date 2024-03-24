# I made this to rememebr the shit that I have learned in python

# MAKING AN INDEPENDENT LIST VARIABLE FROM ANOTHER LIST
# one very big bullshittry i've been expreiencing is when making a list and assigining a value to that list using another list results in it changing aven if i leave it untouched
# turns out u have to use the [:] slice operator to make it independent
from collections import deque
from collections import namedtuple
from collections import Counter
import string
from timeit import default_timer as timer
import timeit
import sys
from itertools import accumulate
from heapq import heapify
from collections import defaultdict
from unicodedata import name
s1 = [1, 2, 3]
s2 = s1[:]

# dictionary tip to reduce else statements when doing this kinda stuff
# basically gets the current val and if its none makes it 0 then adds 1, :)
dic1[item] = dic1.get(item, 0) + 1

# or u can use defaultdict from collections hehehe
# the value passed is the dafualt value in case thing doesnt exist, pretty nifty stuff
d = defaultdict(list)

# so u can add if else statements in python for loop conditions
# basically, if the condition below enclosed in the bracket holds true, it uses the number on the left
# if not, then it uses the one on the right, very cool new learning
for _ in range((2, 0)[3 < 4]):
    pass

# another cool thing to learn, this thing is basically a one liner of this one
lambda self, nums: next((i for i, n in enumerate(nums) if n == i % 10), -1)

# this
for i, n in enumerate(nums):
    if n == 1 % 10:
        return i
# return -1

# also, use heaps, good shit

# learn bst traversals and shit

# any oneliner python cool
if any(num == board[y][i] for i in range(9)):
    print(False)
if any(num == board[i][x] for i in range(9)):
    print(False)

# return all
all(x == y for x, y in smth smth)

# also very cool new learning, yield
# its kinda like return, but it doesnt end the excution of the program
# so its useful for stuff like returning lists in a function but you dont want to make additional space for said lists


def c(num):
    while True:
        yield num
        num += 1


c(2)

# accumuate produces a list where every index is the sum of the values of the indices before it
print(accumulate([1, 2, 3], initial=0))

# cool lambda count function
res = reduce(lambda count, i: count + (i % 2 != 0), test_list, 0)


# itertools cycle

# to get an order dict instead of tuple bullshit
collections.orderedDict()

# star can also be used in this case
# this is similar to css flex where l1 gets the first item, l3 gets the last item, and l2 gets everything in between
# this is the most complex u for this particular ability
l1, *l2, l3 = sentence.split()

# if you remember, * can also be used in functions to basically act as a signle variable that will get decontructed
# the function call below can take as many variables as it can


def funct(*args):
    print(args)


funct(1, 2, 3, 4, 5)


def func(*args):
    l1, l2, l3, l4, l5, *l6 = args
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# list is more wasteful bytewise than a tuple cuz it can take an infinite amount of items
t = (1, 2, 3, 4)
l = [1, 2, 3, 4]
sys.getsizeof(t) < sys.getsizeof(l)

# this is a very useful module
# import timeit
print(timeit.timeit(stmt="[1,2,3,4,5]", number=100000))
print(timeit.timeit(stmt="(1,2,3,4,5)", number=100000))

# this is a useful tool for dicts, so i believe this means that a dict also saves the time it was inserted
# delete the last item added onto the list
dict = {"name": "Max", "age": 19}
mydict.popitem()

# this is the same as the list copy copy thingy
s2 = s1[:]
# but this one is for dicts
d2 = d1.copy()
# update method to merge 2 dicts
# this btw overwrites the values with similar keys in d2, it bases the new values to the ones in d1
d2.update(d1)
# you can use a tuple as a key, however, you cannot use a list as a key since its immutable


A = {1, 2, 3}
B = {3, 4, 5}
# for sets, use union to combine
A.union(B)
# if you want intersection then use intersection duh
A.intersection(B)
# just like my sisters lesson, u can use minus on sets, just like the venn diagrams
# case: A.difference(B) ---> using minus will produce the numbers in A that are not in B
A.difference(B)
# u can also use symmeteric_difference to get the values not in both
A.symmetric_difference(B)

# can use these methods to update sets without using a third variable
# basically an update in place
A.update(B)
A.intersection_update(B)
A.difference_update(B)

# u can also use this method to get boolean answer ---> basically all in A must be in B, B is treated the superset that A must be a subset of
A.issubset(B)
# or basically this if its a superset ig
A.issuperset(B)
# if u want to copy, use the same thing used as the one at the top

# frozenset thing cannot be changed after its creation
a = frozenset([1, 2, 3, 4])

# triple quotes can be used to make multiline strings
print("""Hello 
World
Printthis""")
# use \ to escape quotes, just like regex


# u already know this but learn this arcane shit
s = "leetcode string"
s[::-1]  # reverses
s[::2]  # gets every second char
s[::1]  # gets every character default

# good for prefix or suffix
s.startswith("123")
s.endswith("123")

# this is like index, but if it donesnt find a string, it retruns -1 so iz better
s.find('0')

# use replace and regex for smart af shit, the one on the left is what you find, the one on the right is what you replace it with
s.replace("Test", "Leetcode")

# ooooooowwww new learning
# this apparently is bad practice because since a string is immutable, this line of code actually creates a new string, waste of time and space
res = ''
for i in s:
    # this one
    s += i

# use .join at ALL times


# also new good shit, use this
# from timeit import default_time to basically make a stopwatch of some sorts that keep tracks of the time the code is running, useful for check which parts of the code takes a long time to do
lis = ['a'] * 1000000

start = timer()
res = ''
for i in lis:
    res += i
stop = timer()

print(stop - start)

start = timer()
res = ''.join(lis)
stop = timer()

print(stop - start)


# u can format strings using .format in the past, but its already deprecated

# %s ---> string || %d ----> int || %f ----> float
var = "Tom"
s = "the variable is %s" % var

# just like in the past, u can decide how many letters of digits to be added using the %.n method

var = 123.123
s = "the variable is %.2f" % var
# or this
var2 = 123123123.123123123123
s = "this is the variable {:.2f} and this is the next var {:.5f}".format(
    var, var2)

# however like i said this is already deprecated so use the typical javascript like way instead where u use brackets to specify that this is a variable instead of a string but w/o the $
var = 123123.123123
s = f"this is the variable {var} and this is the next {var2}"


# u already know most of this due to leetcode but still learn then sunce they will be VERY usefullllll
# u can use stuff in normal dictoonaries
s = "Hello world"
d = Counter(s)

# u can also do this for the most common, u can add a value as an argument to get the most common shit
# yea baby
# its like that one med hackerrank problem i did was worthless BHAHAHAHAHHA
print(d.most_common(n))

# u can use d.elements() to basically get the elements of the thingy, so like a string thats divided into chars in a list... yea i dont see the point as well

# ooooo this is very cool
# from collections import namedtuple
# so the first arg is the name, typically the one you used as the variable, the 2nd one are the fields in said tuple
Point = namedtuple("Point", "x, y")
pt = Point(1, -3)
# this will print ----> Point(x=1, y=-3)


# ordereddict is already useless kinda since like i said earlier, the recent python dicts already save the time
# basically orders the dict depending on the order u inserted shit, so if u pop, u pop the recently added


# ok this one is very good
# from collections import defaultdict
# this basically assigns a type to a dicts values even before they are made, kinda like typescript i guess
# the default value for int is 0
d = defaultdict(int)

# other types inclide
list  # []
float  # 0.0
string  # ''

# deque to make a queue thats doubly linked i believe, u can access the one at the bottom as well as the one on the top
# from collections import deque
d = deque()
d.append(4)
d.append(5)
d.append(6)

# very typical shit pa i know, but then, u get the point
d.appendleft(3)
d.appendleft(2)
d.appendleft(1)

# this also words
d.pop()
d.popleft()

# extend method adds multiple shit on the right side, but the same can also be done on the left using extend_left
d.extend([6, 7, 8])

# by the way this is bali so yea, this will produce a list thats sorted
d.extendleft([1, 0, -1])
