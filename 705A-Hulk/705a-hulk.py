if __name__ == "__main__":
  n = int(input())
  s = ["I hate ", "that I love ", "that I hate "]
  p = ""
  i = 0
  for _ in range(n):
      if i == 3:
          i = 1
      p += s[i]
      i += 1
  print(p+"it")
