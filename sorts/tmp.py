import os

l = ["Insertion", "Bubble", "Merge", "Radix"]

for s in l:
    if s not in os.listdir():
        os.makedirs(s)