def bitpp():
    x = 0
    n = int(input())
    for _ in range(n):
        oper = input()
        if oper == "++X" or oper == "X++":
            x += 1
        elif oper == "--X" or oper == "X--":
            x -= 1
    print(x)
 
if __name__ == "__main__":
    bitpp()
