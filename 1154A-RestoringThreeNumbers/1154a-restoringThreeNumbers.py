a = list(map(int, input().split()))
a.sort()
x1 = a[0]
x2 = a[1]
x3 = a[2]
x4 = a[3]
a = x4 - x3
b = x1 - x4 + x3
c = x4 - x1
print(f"{a} {b} {c}")
