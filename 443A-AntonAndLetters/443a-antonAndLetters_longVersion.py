if __name__ == "__main__":
  i = set(input()[1:-1].split(', '))
  if list(i)[0] == '':
      print(0)
  else:
      print(len(i))
