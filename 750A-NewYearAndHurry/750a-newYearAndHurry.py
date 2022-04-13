p = list(map(int, input().split()))
n = p[0]
org_n = n
k = p[1]
time_left = 240 - k
i = 1
while time_left >= 0 and n > 0:
    time_left -= 5*i
    if time_left < 0:
        break
    n -= 1
    i += 1
print(org_n - n)
