n = int(input())
a = list(map(int, input().split()))
least = a[0]
most = a[0]
counter = 0
for num in a:
    if num > most:
        most = num
        counter += 1
    elif num < least:
        least = num
        counter += 1
print(counter)
