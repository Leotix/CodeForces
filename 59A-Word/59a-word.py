if __name__ == "__main__":
  x = input()
  up = 0
  low = 0
  for item in x:
      if item.islower():
          low += 1
      else:
          up += 1
  if up > low:
      print(x.upper())
  else:
      print(x.lower())
