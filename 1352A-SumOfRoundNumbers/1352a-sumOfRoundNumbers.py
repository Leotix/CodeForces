for _ in range(int(input())):
    p = input()
    p = [int(x) for x in p][::-1]
    for i in range(len(p)):
        p[i] *= 10**i
    p = [x for x in p if x != 0]
    print(len(p))
    print(*p)
 
