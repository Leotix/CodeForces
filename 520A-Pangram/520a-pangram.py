import string
if int(input()) < 26:
    print("NO")
    exit(0)
else:
    s = list(input().lower())
    for char in list(string.ascii_lowercase):
        if char not in s:
            print("NO")
            exit(0)
print("YES")
