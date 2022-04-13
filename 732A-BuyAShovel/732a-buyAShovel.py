h, i, j = 1, 0, 1
k, r = [int(x) for x in input().split()]
while True:
    i += 1
    h = k * i
    if h % 10 == 0 or h % 10 == r:
        break
print(i)
