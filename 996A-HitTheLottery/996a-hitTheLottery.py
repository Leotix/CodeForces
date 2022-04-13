n = int(input())
billsCount = 0
bills = [100, 20, 10, 5, 1]
for bill in bills:
    divided = n//bill
    billsCount += divided
    n -= divided*bill
print(billsCount)
