def reverse(number):
    s = ""
    for character in number:s = character + s
    return int(s)    

number = 0
while number != 10000:
    if reverse(str(number)) + 450 == number:print(number)
    number += 1
