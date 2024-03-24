n = input().strip()
reversed_n = ""
for x in range(len(n) - 1, -1, -1):
    reversed_n += n[x]

count = 0
string = ""
for x in reversed_n:
    string += x
    count += 1
    if count == 3:
        string += ","
        count = 0

reversed_string = ""
for x in range(len(string) - 1, -1, -1):
    reversed_string += string[x]
if reversed_string[0] == ",":
    reversed_string = reversed_string[1:]
print(reversed_string)