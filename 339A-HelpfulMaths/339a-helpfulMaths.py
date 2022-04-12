if __name__ == "__main__":
  s = input().split('+')
  if len(s) == '1':
      print(s[0])
  else:
      s.sort()
      print('+'.join(s))
