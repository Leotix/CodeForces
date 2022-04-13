if __name__ == "__main__":
  s = input()
  lst = [char for char in s]
  mySet = set(lst)
  if len(mySet) % 2 == 1:
      print("IGNORE HIM!")
  else:
      print("CHAT WITH HER!")
