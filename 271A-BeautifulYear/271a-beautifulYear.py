if __name__ == "__main__":  
  y = input()
  first = int(y)
  while True:
      y = str(y)
      lst = [int(x) for x in y]
      if len(set(lst)) == 4 and int(y) != first:
          print(y)
          break
      y = int(y)
      y += 1
