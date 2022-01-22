a = 0
b = {3, 6, 9}
for a in b:
    print("*")
    a += 1
    if a not in b:
        a += 1
        print(a)
