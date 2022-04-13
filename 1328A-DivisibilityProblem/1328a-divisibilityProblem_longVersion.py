if __name__ == "__main__":
    lst = []
    for _ in range(int(input())):
        p = [int(x) for x in input().split()]
        if p[0] % p[1] == 0:
            lst.append(0)
        else:
            lst.append(p[1] - p[0] % p[1])
    for num in lst:
        print(num)
