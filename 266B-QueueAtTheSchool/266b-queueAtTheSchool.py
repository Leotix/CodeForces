if __name__ == "__main__":
  x = input().split()
  n = int(x[0])
  t = int(x[1])
  s = input()
  s = list(s)

  while t != 0:
      i = 0
      while i < n - 1:
          if s[i] == 'B' and s[i+1] == 'G':
              s[i], s[i+1] = s[i+1], s[i]
              if i != n - 2:
                  i += 1
          i += 1
      t -= 1
  s = ''.join(s)
  print(s)
