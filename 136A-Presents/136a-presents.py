if __name__ == "__main__":
  n = int(input())
  j = input().split()
  tmp = []
  i = 1
  for _ in range(len(j)):
      tmp.append(str(j.index(str(i))+1))
      i += 1
  print(' '.join(tmp))
