x = input()
res = ""
helper = False
for i in range(len(x)):
    if helper:
        helper = False
        continue
    if x[i] == ".":
        res += "0"
    elif x[i] + x[i+1] == "-.":
        res += "1"
        helper = True
        continue
    elif x[i] + x[i+1] == "--":
        res += "2"
        helper = True
        continue
print(res)
