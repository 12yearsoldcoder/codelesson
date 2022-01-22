a = int(input())
b = int(input())
c = a * (b % 10)
d = a * (b // 10 * 10 % 100 // 10)
e = a * (b // 100 * 100) // 100
print(c, d, e,c+b*100+e*100)
