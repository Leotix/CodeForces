n = int(input())
tab = [int(x) for x in input().split()]
readyToWork = 0
untreatedCrimes = 0
for i in tab:
    if i > 0:
        readyToWork += i
    else:
        if readyToWork > 0:
            readyToWork -= 1
        else:
            untreatedCrimes += 1
print(untreatedCrimes)
