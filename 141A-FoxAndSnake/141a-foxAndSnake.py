word = list(input())
word.extend(list(input()))
t = list(input())
if len(word) > len(t):
    print("NO")
    exit(0)
for i in range(len(word)):
    try:
        t.remove(word[i])
    except:
        pass
if len(t) != 0:
    print("NO")
else:
    print("YES")
del word, t
