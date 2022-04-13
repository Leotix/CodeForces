if __name__ == "__main__":
  for _ in range(int(input())):
    p, a, b, c = map(int, input().split())
    print(min(-p % a, -p % b, -p % c))
