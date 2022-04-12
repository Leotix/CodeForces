if __name__ == "__main__":
    x = input().lower()
    y = input().lower()
    if y > x:
        print(-1)
    elif x > y:
        print(1)
    else:
        print(0)
