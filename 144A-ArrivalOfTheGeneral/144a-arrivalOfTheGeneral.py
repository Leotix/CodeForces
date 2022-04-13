if __name__ == "__main__":
  n = int(input())
  s = [int(x) for x in input().split()]
  p = s.index(max(s)) + s[::-1].index((min(s)))
  print(p - int(p >= n))
