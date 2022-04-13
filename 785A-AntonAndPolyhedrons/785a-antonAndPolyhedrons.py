counter = 0
polyhendrons = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
for _ in range(int(input())):
    counter += polyhendrons.get(input())
print(counter)
