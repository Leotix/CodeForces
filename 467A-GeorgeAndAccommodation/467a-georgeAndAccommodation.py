if __name__ == "__main__":
  x = int(input())
  i = 0
  for _ in range(x):
      y = input().split()
      p = int(y[0])
      q = int(y[1])
      if q - p >= 2:
          i += 1
  print(i)
