n = input().strip()
count = 3 - len(n) % 3
if count == 3: count = 0
string = ""
for x in range(len(n)):
    string += n[x]
    count += 1
    if count == 3 and x != len(n) - 1:
        string += ","
        count = 0
print(string)