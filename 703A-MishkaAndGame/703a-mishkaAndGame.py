mishka_points = 0
chris_points = 0
for _ in range(int(input())):
    points = [int(x) for x in input().split()]
    if points[0] > points[1]:
        mishka_points += 1
    elif points[0] < points[1]:
        chris_points += 1
    else:
        continue
if mishka_points > chris_points:
    print("Mishka")
elif mishka_points < chris_points:
    print("Chris")
else:
    print("Friendship is magic!^^")
