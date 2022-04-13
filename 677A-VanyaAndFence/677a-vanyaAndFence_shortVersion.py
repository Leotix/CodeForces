if __name__ == "__main__":
  h = int(input().split()[1])
  s = input().split()
  print(sum([(int(int(i) > h) + 1) for i in s]))
