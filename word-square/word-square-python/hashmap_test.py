# hashmap = {}
#
# for i in range(100000):
#     hashmap[i] = i
#
# for i in range(100000):
#     if i in hashmap:
#         print(hashmap[i])
#     else:
#         print("Valuue is not in hashmap")


arr = [0] * 100000

for i in range(100000):
    arr[i] = i

for i in range(100000):
    print(f"Value at index {i} is {arr[i]}")
