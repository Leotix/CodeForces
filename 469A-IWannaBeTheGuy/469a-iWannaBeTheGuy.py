if __name__ == "__main__":
  n = int(input())
  p = input().split()
  q = input().split()
  if len(set(p[1:]+q[1:])) == n:
      print("I become the guy.")
  else:
      print("Oh, my keyboard!")
