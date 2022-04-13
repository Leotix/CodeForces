for _ in range(int(input())):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    print(int((abs(a - b)+9)/10))
