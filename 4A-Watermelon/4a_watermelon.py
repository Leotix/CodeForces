def canBeEvenPieces():
  x = int(input())
  if x < 1 or x > 100:
      return
  if x % 2 == 0 and x//2 > 1:
      print('YES')
  else:
      print('NO')
 
if __name__ == "__main__":
  canBeEvenPieces()
