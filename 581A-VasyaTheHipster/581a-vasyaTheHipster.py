ab = list(map(int, input().split()))
a = ab[0]
b = ab[1]
if a > b:
    print(f"{b} {(a - b) // 2}")
else:
    print(f"{a} {(b - a) // 2}")
