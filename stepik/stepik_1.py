a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(a, b + 1):
    print('\t', j, end="")
for i in range(c, d + 1):
    print('\t', i)

for i in range(c, d + 1):
    for j in range(a,b+1):
        print(f'{i * j : 4}', end=" ")
    print()

#