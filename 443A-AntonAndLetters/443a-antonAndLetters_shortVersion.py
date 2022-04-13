if __name__ == "__main__":
  print((lambda x: len(set(x.split(', '))) if x != '' else 0)(input()[1:-1]))
