if __name__ == "__main__":
  _list = [input() for _ in range(int(input()))]
  print(1 + len([True for x, y in zip(_list, _list[1:]) if x != y]))
