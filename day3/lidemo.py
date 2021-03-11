a = [12,24,25,63,21,130]

# k = 0
# while k <= 5:
#     print(a[k])
#     k = k + 1

# 求列表中的最大值
max = 0
k = 0
while k <= 5:
    if a[k] > max:
        max = a[k]
    k = k + 1

print(max)


