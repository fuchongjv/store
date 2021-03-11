a = [1, 5, 21, 30, 15, 9, 30, 24]
i = 0
sum = 0
while i <= 7:
    if a[i] % 5 == 0:
        sum += a[i]
    i += 1
print(sum)
