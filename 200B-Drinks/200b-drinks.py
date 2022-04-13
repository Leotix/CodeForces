if __name__ == "__main__":
  n = int(input())
  p = list(map(int, input().split()))
  print("%.12f" % (sum(p) / n))
