if __name__ == "__main__":
  s = input().split()
  n = int(s[0])
  k = int(s[1])

  for _ in range(k):
      if n % 10 != 0:
          n -= 1
      else:
          n = n//10
  print(n)
