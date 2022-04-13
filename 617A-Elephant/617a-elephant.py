if __name__ == "__main__":
    x = int(input())
    counter = 0
     
    for i in range(5,0,-1):
        while x - i >= 0:
            counter += 1
            x -= i
    print(counter)
