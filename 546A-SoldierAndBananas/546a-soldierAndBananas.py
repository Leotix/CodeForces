if __name__ == "__main__":
  s = input().split()
  k = int(s[0])
  n = int(s[1])
  w = int(s[2])
  cost = 0
  for i in range(1, w+1):
      cost += i*k
  if cost > n:
      print(cost-n)
  else:
      print(0)
