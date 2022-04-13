if __name__ == "__main__":
  n1 = [int(x) for x in input()]
  n2 = [int(x) for x in input()]
  res = []
  for i in range(len(n2)):
      res.append(str(n1[i] ^ n2[i]))
  print(''.join(res))
