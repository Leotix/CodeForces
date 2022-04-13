if __name__ == "__main__":
  lst = 0
  n = int(input())
  colors = input()
  for i in range(len(colors)-1):
      if colors[i] == colors[i+1]:
          lst += 1
  print(lst)
