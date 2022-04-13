def fun():
    for i in range([int(x) for x in input().split()][0]):
        if any(color in ["C", "M", "Y"] for color in [x for x in input().split()]):
            print("#Color")
            return
    print("#Black&White")
fun()
