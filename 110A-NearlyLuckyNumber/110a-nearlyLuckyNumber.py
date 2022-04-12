if __name__ == "__main__":
  k = input()
  n = [int(x) for x in k]

  lucky = 0
  for num in n:
      if num == 4 or num == 7:
          lucky += 1
  if lucky == 4 or lucky == 7:
      print("YES")
  else:
      print("NO")
