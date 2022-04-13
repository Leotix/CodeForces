if __name__ == "__main__":
  tmp = input().split()
  n = int(tmp[0])
  h = int(tmp[1])
  c = 0

  tmp = input().split()
  a = [int(x) for x in tmp]
  for num in a:
      if num > h:
          c += 2
      else:
          c += 1
  print(c)
