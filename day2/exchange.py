a = 56
b = 78

a = a + b
b = a - b   # b = (a + b) - b = a
a = a - b   # a = (a + b) - a = b

print(a, b)
