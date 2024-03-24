k = int(input().strip())
list1 = map(int, input().strip().split())
list2 = map(int, input().strip().split())

print((k in list1 and k not in list2) or (k in list2 and k not in list1))