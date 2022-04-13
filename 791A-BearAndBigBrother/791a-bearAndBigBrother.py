if __name__ == "__main__":
  weights = input().split()
  limak = int(weights[0])
  bob = int(weights[1])

  i = 0
  while(True):
      limak = 3*limak
      bob = 2*bob
      i += 1
      if limak > bob:
          print(i)
          break
