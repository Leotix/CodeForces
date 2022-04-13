x = [int(x) for x in input().split()]
 
def swap(x):
    tmp = x[0]
    x[0]=x[1]
    x[1]=x[2]
    x[2]=tmp
p=0
while True:
    if x[0] <= x[1] <= x[2] or x[2] <= x[1] <= x[0]:
        p = x[1]
        break
    else:
        swap(x)
p1 = abs(p - x[0])
p2 = abs(p - x[2])
distance = p1 + p2
print(distance)
