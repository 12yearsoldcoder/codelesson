a = int(input())
O = 0
X = 0
for i in range(a):
    b = str(input())
    while "O" in b:
        O += 1
        while "X" in b:
            X += 0
    print(O + X)
