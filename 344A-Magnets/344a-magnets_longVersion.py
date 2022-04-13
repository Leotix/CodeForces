if __name__ == "__main__":
  n = int(input())
  a = []
  for _ in range(n):
      a.append(input())
  counter = 1
  for i in range(n-1):
      if a[i] != a[i+1]:
          counter += 1
  print(counter)
