exp = input()
exp = list(exp)

if "+" in exp:
    number = ""
    c = False
    for x in range(len(exp)):
        if exp[x] in ["+", "-", "*", "/"]:
            if exp[x] == "+" and c == False:
                exp[x-len(number)] = "(" + exp[x-len(number)]
                c = True
            elif c == True and exp[x] != "+":
                exp[x] = ")" + exp[x]
                c = False
            number = ""
        else:
            number += exp[x]

if c == True:
    exp.append(")")

print(''.join(exp))
print(eval(''.join(exp)))